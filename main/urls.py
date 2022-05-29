from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("<str:category>/", views.project_category, name="project_category"),
]