from .models import *
from django.views.generic import ListView


class PointsTable(ListView):
    model = Points
    template_name = "figureSkaters/detailResult.html"
    context_object_name = "list_elements"


class ResultTable(ListView):
    model = Result
    template_name = "figureSkaters/result.html"
    context_object_name = "list_skaters"


class ListCompetition(ListView):
    model = Competition
    template_name = "figureSkaters/Competition.html"
    context_object_name = "list_of_competition"
