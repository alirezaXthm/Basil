from django.urls import path
from .views import  fill_form
from . import views


urlpatterns = [
    path('tour/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('fill-form/<int:tour_id>/', fill_form, name='fill_form'),
    path('', views.home, name='home'),
]
