from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home_view(request):
    return HttpResponse("Hello, World!")


def about_view(request):
    return JsonResponse({"message": "Hello, World!"})
