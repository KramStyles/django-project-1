from django.urls import path

from . import views

urlpatterns = [
    path('jan', views.january),
    path('<int:num_months>', views.num_month),
    path('<str:month>', views.monthly_tasks),
    path('', views.home)
]
