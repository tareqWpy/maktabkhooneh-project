from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from accounts.forms import RegisterForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if "next" in request.POST:
                        messages.success(request, "You logged in successfully! 😀")
                        return redirect(request.POST.get("next"))
                    else:
                        messages.success(request, "You logged in successfully! 😀")
                        return redirect("/")
                else:
                    messages.error(
                        request, "Invalid username or password. Please try again! ❌"
                    )
            else:
                messages.error(
                    request,
                    "Invalid form submission. Please check the entered data! ❌",
                )
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    else:
        return redirect("/")


@login_required
def logout_view(request):
    logout(request)
    messages.success(
        request,
        "You logged out successfully!",
    )
    return redirect("/")


from django.contrib import messages


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "You signed up successfully! ✅")
                return redirect("accounts:login")
            else:
                messages.error(
                    request, "Errors in the form. Please correct them and try again!❌"
                )

        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/signup.html", context)
    else:
        return redirect("/")
