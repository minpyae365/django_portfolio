from django.urls import path
from exercises import views

urlpatterns = [
    path('', views.exercise_index, name='exercise_index'),
    path("<int:pk>/", views.exercise_detail, name="exercise_detail"),
    path("<str:category>/", views.exercise_category, name="exercise_category"),
]