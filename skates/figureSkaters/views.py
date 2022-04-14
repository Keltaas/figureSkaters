from .models import *
from django.views.generic import ListView


class PointsTable(ListView):
    model = Points
    template_name = "figureSkaters/base.html"
    context_object_name = "list_elements"


class ResultTable(ListView):
    model = Result
    template_name = "figureSkaters/result.html"
    context_object_name = "list_skaters"
