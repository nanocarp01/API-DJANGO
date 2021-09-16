from django.urls import path
from .views import APIpListViews, APIpDetailViews


urlpatterns = [
    path('project/', APIpListViews.as_view(), name='project-list'),
    path('project/<int:pk>/', APIpDetailViews.as_view(), name='project-detail'),
]