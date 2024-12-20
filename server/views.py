from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .controller import get_users_data
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return HttpResponse('Welcome to server postgreSQL')

@csrf_exempt
def fetch_users_data(request):
    if request.method == "GET":
        users = get_users_data()

        users = list(users.values())

        return JsonResponse(users, safe=False)