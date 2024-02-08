from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("idCard", views.upload_image, name="idCard"),
]