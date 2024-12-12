from django.urls import path
from calciapp import views

urlpatterns=[
    path('',views.index),
    path('result',views.result)
]