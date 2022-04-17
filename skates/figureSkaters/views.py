from .models import *
from django.views.generic import ListView, DetailView


class PointsTable(ListView):
    model = Points
    template_name = "figureSkaters/detailResult.html"
    context_object_name = "list_elements"


class ResultTable(ListView):
    model = Result
    template_name = "figureSkaters/result.html"
    context_object_name = "list_skaters"

    def get_queryset(self):
        return Result.objects.filter(competition__pk=self.kwargs.get("slug", None))


class ListCompetition(ListView):
    model = Competition
    template_name = "figureSkaters/Competition.html"
    context_object_name = "list_of_competition"


class Categories(ListView):
    model = CategoriesOfCompetition
    template_name = "figureSkaters/category_of_competition.html"
    context_object_name = "categories"

    def get_queryset(self):
        return CategoriesOfCompetition.objects.filter(competition__pk=self.kwargs.get("pk", None))
