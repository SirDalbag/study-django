from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from django_app import models, serializers
from django.db.models import QuerySet

@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "OK"})

@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def get_contracts(request):
    contracts = models.Contract.objects.all()
    _serializer = serializers.ContractsSerializer(contracts, many=True).data
    return Response(data={"message": _serializer})