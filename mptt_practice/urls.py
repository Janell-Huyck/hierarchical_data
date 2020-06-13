from django.urls import path
from mptt_practice import views

urlpatterns = [path('', views.index, name='home')]
