from rest_framework import serializers
from django_app import models


class PersonSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    class Meta:
        model = models.Person
        exclude = ["id"]

    @staticmethod
    def get_position(obj):
        try:
            return obj.position.title
        except Exception as error:
            return str(error)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClothCategory
        fields = "__all__"


class ClothSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cloth
        fields = "__all__"
