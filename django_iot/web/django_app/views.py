from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_app import models
from os import getenv
import requests

TOKEN = getenv("TOKEN")
USERS = ["969075792"]


def index(request):
    return render(request, "index.html")


@api_view(http_method_names=["GET", "POST"])
def api(request):
    if request.method == "GET":
        return Response(
            data=[f"{x.serial_id}:{x.is_working}" for x in models.Vehicle.objects.all()]
        )
    elif request.method == "POST":
        try:
            data = request.data
            alarm = False
            for vehicle in data:
                models.Vehicle.objects.create(**vehicle)
                if not vehicle["is_working"]:
                    alarm = True
            if alarm:
                message = "Attention!"
                for user in USERS:
                    response = requests.post(
                        url=f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                        json={"chat_id": user, "text": message},
                    )
            return Response(data={"message": "OK"})
        except Exception as error:
            return Response(data={"message": error})
