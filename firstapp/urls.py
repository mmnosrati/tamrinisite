from django.urls import path
from firstapp import views

urlpatterns = [path("test_path", views.test_view)]
