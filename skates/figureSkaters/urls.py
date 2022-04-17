from .views import *
from django.urls import path


urlpatterns = [
    path("", PointsTable.as_view(), name="home"),
    path("result/<slug:slug>", ResultTable.as_view(), name="result"),
    path("competitions/", ListCompetition.as_view(), name="competitions"),
    path("competition/<int:pk>", Categories.as_view(), name="categories"),
]
