from django.urls import path
from .views import community_stats

urlpatterns = [
    path('community-stats/', community_stats), # This matches what React wants
]