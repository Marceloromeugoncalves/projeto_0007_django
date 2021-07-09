from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RichPerson


"""
class RichPersonView(TemplateView):
    template_name = 'rich_people/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_set"] = RichPerson.objects.all()
        return context
"""

def home(request):
    chart_type = request.GET.get('chart_type')
    query_set = RichPerson.objects.all()

    if chart_type is None:
        chart_type = 'bar'

    context = {
        'chart_type': chart_type,
        'query_set': query_set,
    }

    return render(request, 'rich_people/chart.html', context)




