from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from accounts.forms import MyUserCreationForm


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
                        return redirect(request.POST.get("next"))
                    else:
                        return redirect("/")
        messages.success(
            request,
            "You logged in successfully!",
        )
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


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("accounts:login")
        messages.success(
            request,
            "You signed up successfully!",
        )
        form = MyUserCreationForm()
        context = {"form": form}
        return render(request, "accounts/signup.html", context)
    else:
        return redirect("/")
