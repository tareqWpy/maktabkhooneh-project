from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from projectApp.forms import ContactForm, NewsletterForm
from projectApp.models import Contact


def home_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact has been created successfully! 🎉")
        else:
            messages.error(
                request, "Failed to create a contact. Please check your input. 🚫"
            )
    else:
        form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


"""
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your ticket submitted successfully!"
            )
        else:
            messages.add_message(request, messages.ERROR, "Your ticket did not submit!")
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})
"""


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your email submited successfully!",
            )
            return HttpResponseRedirect("/")

    elif request.method == "GET":
        return HttpResponseRedirect("/")
