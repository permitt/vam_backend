from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='menu_general_url'),
    path('menu/<int:id>/', views.MenuView.as_view(), name='menu_specific_url'),

]
