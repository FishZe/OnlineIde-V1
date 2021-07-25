from django.urls import path

from . import views

urlpatterns = [
    path('judge', views.Judge)
]
