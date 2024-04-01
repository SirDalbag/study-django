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


class ReportSerializer(serializers.ModelSerializer):
    tabel_num = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    cloth = serializers.SerializerMethodField()

    class Meta:
        model = models.ClothSet
        fields = ["tabel_num", "last_name", "cloth", "created_at"]

    @staticmethod
    def get_tabel_num(obj):
        try:
            return obj.person.tabel_num
        except Exception as error:
            return str(error)

    @staticmethod
    def get_last_name(obj):
        try:
            return obj.person.last_name
        except Exception as error:
            return str(error)

    @staticmethod
    def get_cloth(obj):
        try:
            return obj.cloth_type.title
        except Exception as error:
            return str(error)
