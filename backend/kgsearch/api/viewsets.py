from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from . import serializers
from kgsearch import models
import pickle

class SearchViewset(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    
    def get_queryset(self):
        return models.Dataset.objects.all()
    
    def get_serializer_class(self):
        return serializers.DatasetList
    
    @action(methods=['GET'], detail=True)
    def search(self, request, *args, **kwargs):
        obj = self.get_object()
        with open(obj.pkl.path, 'rb') as f:
            search = pickle.load(f)
        data = request.GET
        return Response(search(query=data.get('q'), k=int(data.get('k')), n=int(data.get('k')), p=int(data.get('k'))), status=200)