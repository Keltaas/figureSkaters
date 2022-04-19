from .views import *
from django.urls import path


urlpatterns = [
    path("", ListCompetition.as_view(), name="home"),
    path("detail/", PointsTable.as_view(), name="detail"),
    path("result/", ResultTable.as_view(), name="result"),
    path("competitions/", ListCompetition.as_view(), name="competitions"),
    path("competition/<int:pk>", Categories.as_view(), name="categories"),
]
