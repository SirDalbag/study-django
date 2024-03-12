from rest_framework import serializers
from django_app import models


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = "__all__"