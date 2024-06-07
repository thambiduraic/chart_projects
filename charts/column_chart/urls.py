from django.urls import path
from . import views

urlpatterns = [
    path('column_chart', views.index),
    path('multi_column_chart', views.multi_column_view)
]
