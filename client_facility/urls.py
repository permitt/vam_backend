from django.urls import path
from . import views


urlpatterns = [
    path('facility/', views.ClientFacilityView.as_view(), name='facility_general_url'),
    path('facility/<int:id>/', views.ClientFacilityView.as_view(), name='facility_specific_url')
]
