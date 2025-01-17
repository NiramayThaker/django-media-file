from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_form, name='form'),
    path("dogs", views.list_dogs, name='all-dogs'),
    path("delete_dogs/<int:pk>/", views.delete_dogs, name='delete-image'),
]
