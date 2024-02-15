from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
def api(request):
    return Response(data={"message": "OK"})
