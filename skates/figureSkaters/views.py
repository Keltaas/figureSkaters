from .models import *
from django.views.generic import ListView, DetailView


class PointsTable(ListView):
    model = Points
    template_name = "figureSkaters/detailResult.html"
    context_object_name = "list_elements"

    def get_queryset(self):
        segment_id = self.request.GET.get("segment")
        if segment_id == "1":
            segment = "Short Program"
        else:
            segment = "Free Skating"
        return Points.objects.filter(skater__pk=self.request.GET.get("skater", None), segment__name=segment)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["object_list"]:
            context["skater"] = context["object_list"][0].skater
            context["competition"] = context["object_list"][0].competition
        return context


class ResultTable(ListView):
    model = Result
    template_name = "figureSkaters/result.html"
    context_object_name = "list_skaters"

    def get_queryset(self):
        return Result.objects.filter(competition__pk=self.request.GET.get("competition", None),
                                     skater__category__pk=self.request.GET.get("category", None))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["object_list"]:
            context["competition"] = context["object_list"][0].competition
        return context


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
