from rest_framework import serializers
from kgsearch import models

class DatasetList(serializers.ModelSerializer):
    class Meta:
        model = models.Dataset
        fields = ['id', 'name']