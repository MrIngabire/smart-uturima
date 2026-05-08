from django.db import models
from django.contrib.auth.models import User

# REMOVE the import from here (Line 4)

class Garden(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.location}"

class CropRecord(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, related_name='records')
    crop_type = models.CharField(max_length=100)
    soil_moisture = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # MOVE THE IMPORT HERE (Local Import)
        from .agri_engine import run_automation_check
        run_automation_check(self)

class MaintenanceTask(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    action_required = models.CharField(max_length=255)
    is_automated = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)