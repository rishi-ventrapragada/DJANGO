#quiz/urls.py (app level)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('result/', views.result_view, name='result'),
]
