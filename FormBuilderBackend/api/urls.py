from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloWorldApiView.as_view(), name='hello'),
]
