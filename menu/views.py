from django.shortcuts import render
from django.http import JsonResponse
from .models import DishModel

def home(request):
    dishes = list(DishModel.objects.all().values())
    return JsonResponse({"dishes": dishes})
