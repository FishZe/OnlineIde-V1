from django.urls import path

from . import views

urlpatterns = [
    path('run', views.Run),
    path("logincheck", views.Login),
    path('register', views.register)
]
