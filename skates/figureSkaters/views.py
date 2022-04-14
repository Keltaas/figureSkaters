from .models import Points
from django.views.generic import ListView


class PointsTable(ListView):
    model = Points
    template_name = "figureSkaters/base.html"
    context_object_name = "list_elements"
