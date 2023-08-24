from django.urls import path

from . import views
from .views import TemperatureDataView

urlpatterns = [
    path('temperature/', TemperatureDataView.as_view(), name='temperature_data'),
    path('', views.index)
]
