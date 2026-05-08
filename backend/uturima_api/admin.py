from django.contrib import admin
from .models import Garden, CropRecord, MaintenanceTask

# This makes your tables appear in the admin dashboard
admin.site.register(Garden)
admin.site.register(CropRecord)
admin.site.register(MaintenanceTask)