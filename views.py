from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    return render(request, 'booktest/index.html', {'name': 2})



