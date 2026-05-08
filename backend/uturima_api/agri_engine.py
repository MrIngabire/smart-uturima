from .models import MaintenanceTask

def run_automation_check(record):
    if record.soil_moisture < 30:
        # Avoid creating duplicate tasks for the same low-moisture event
        exists = MaintenanceTask.objects.filter(
            garden=record.garden, 
            is_resolved=False, 
            action_required__icontains=record.crop_type
        ).exists()
        
        if not exists:
            MaintenanceTask.objects.create(
                garden=record.garden,
                action_required=f"URGENT: Water the {record.crop_type} (Moisture at {record.soil_moisture}%)",
                is_automated=True
            )
            return True
    return False