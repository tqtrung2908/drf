from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.ListCreateCategoryView.as_view()),
    path('categories/<int:pk>', views.UpdateDeleteCategoryView.as_view()),
]