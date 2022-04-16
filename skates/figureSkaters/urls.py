from .views import *
from django.urls import path


urlpatterns = [
    path("", PointsTable.as_view()),
    path("result/<slug:slug>", ResultTable.as_view()),
    path("competition/", ListCompetition.as_view()),
]
