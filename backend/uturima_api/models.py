from django.db import models
from django.contrib.auth.models import User

class Garden(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.username}'s Garden in {self.location}"

class CropRecord(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, related_name='records')
    crop_type = models.CharField(max_length=100)
    soil_moisture = models.IntegerField() # 0-100
    recorded_at = models.DateTimeField(auto_now_add=True)

class MaintenanceTask(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    action_required = models.CharField(max_length=255)
    is_automated = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
