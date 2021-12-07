from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order_general_url'),
    path('order/<int:id>/', views.OrderView.as_view(), name='order_specific_url'),
]
