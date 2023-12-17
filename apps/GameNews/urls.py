from django.urls import path
from .views import GameNewsListView

urlpatterns = [
    path('lista-GameNews', GameNewsListView.as_view(), name= 'lista-GameNews')
    ]