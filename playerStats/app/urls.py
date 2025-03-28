# Urls created just to the App
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app , name = 'app'),
    path('app/details/<int:id>', views.details, name = 'details')
]
