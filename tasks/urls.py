from django.urls import path

from . import views

urlpatterns = [
    path('jan', views.january),
    path('feb', views.february),
    path('<month>', views.monthly_tasks)
]
