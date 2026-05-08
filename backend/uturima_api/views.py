from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Garden, CropRecord, MaintenanceTask
from .agri_engine import run_automation_check
from rest_framework import serializers

# Simple Serializer
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropRecord
        fields = '__all__'

class CropViewSet(viewsets.ModelViewSet):
    queryset = CropRecord.objects.all()
    serializer_class = CropSerializer

    def perform_create(self, serializer):
        record = serializer.save()
        run_automation_check(record)

@api_view(['GET'])
def community_stats(request):
    return Response({
        "total_gardens": Garden.objects.count(),
        "active_alerts": MaintenanceTask.objects.filter(is_resolved=False).count(),
        "auto_tasks": MaintenanceTask.objects.filter(is_automated=True).count()
    })
