from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def main(request):
    return render(request, "main.html")


def board_list(request):
    return render(request, "board_list.html")


def board_create(request):
    return render(request, "board_create.html")
