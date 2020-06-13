from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('page_two/', views.page_two, name='page-two')
]
