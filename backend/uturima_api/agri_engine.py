from .models import MaintenanceTask

def run_automation_check(record):
    # If moisture is below 30%, auto-create a task
    if record.soil_moisture < 30:
        MaintenanceTask.objects.create(
            garden=record.garden,
            action_required=f"URGENT: Water the {record.crop_type} (Moisture at {record.soil_moisture}%)",
            is_automated=True
        )
        return True
    return False