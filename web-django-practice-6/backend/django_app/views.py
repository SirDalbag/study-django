from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from django_app import models, serializers
from django.utils import timezone
from django.db.models import (
    F,
    ExpressionWrapper,
    DateTimeField,
    DurationField,
    IntegerField,
)
import json
from datetime import timedelta


def index(request):
    return render(request, "index.html")


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_persons(request):
    objects = models.Person.objects.all()
    sort = request.GET.get("sort", None)
    if sort:
        objects = objects.order_by(*sort.split(","))
    filter = request.GET.get("filter", None)
    if filter:
        objects = objects.filter(**json.loads(filter))
    return Response(
        data={"data": serializers.PersonSerializer(objects, many=True).data}
    )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_person(request, id):
    object = models.Person.objects.get(tabel_num=id)
    return Response(
        data={"data": serializers.PersonSerializer(object, many=False).data}
    )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_categories(request):
    objects = models.ClothCategory.objects.all()
    sort = request.GET.get("sort", None)
    if sort:
        objects = objects.order_by(*sort.split(","))
    filter = request.GET.get("filter", None)
    if filter:
        objects = objects.filter(**json.loads(filter))
    return Response(
        data={"data": serializers.CategorySerializer(objects, many=True).data}
    )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_category(request, id):
    object = models.ClothCategory.objects.get(id=id)
    return Response(
        data={"data": serializers.CategorySerializer(object, many=False).data}
    )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_clothes(request):
    objects = models.Cloth.objects.all()
    sort = request.GET.get("sort", None)
    if sort:
        objects = objects.order_by(*sort.split(","))
    filter = request.GET.get("filter", None)
    if filter:
        objects = objects.filter(**json.loads(filter))
    return Response(data={"data": serializers.ClothSerializer(objects, many=True).data})


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_cloth(request, id):
    object = models.Cloth.objects.get(id=id)
    return Response(data={"data": serializers.ClothSerializer(object, many=False).data})


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def post_data(request):
    print(request.data.get("tabel_num"))
    person = models.Person.objects.get(tabel_num=request.data.get("tabel_num"))
    cloth_type = models.Cloth.objects.get(id=request.data.get("clothes"))
    object = models.ClothSet.objects.create(person=person, cloth_type=cloth_type)
    return Response("OK")


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_data(request):
    object = models.ClothSet.objects.all()
    return Response(data={"data": serializers.ReportSerializer(object, many=True).data})


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def get_warning(request):
    now = timezone.now() + timedelta(days=3)
    object = models.ClothSet.objects.all()
    temp = []
    for i in object:
        if i.created_at + timedelta(days=i.cloth_type.deadline) < now:
            temp.append(i)

    temp_filter = models.ClothSet.objects.annotate(
        days=ExpressionWrapper(F("cloth_type__deadline"), output_field=IntegerField()),
        end_date=F("created_at")
        + ExpressionWrapper(
            F("days") * timedelta(days=1), output_field=DurationField()
        ),
    ).filter(end_date__lte=now)
    return Response(
        data={"data": serializers.ReportSerializer(temp_filter, many=True).data}
    )
