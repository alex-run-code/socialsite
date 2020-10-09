from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<id>/<slug>/', views.image_detail, name='detail'),
]