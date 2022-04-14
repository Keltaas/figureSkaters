from .views import *
from django.urls import path


urlpatterns = [
    path("", PointsTable.as_view()),
]