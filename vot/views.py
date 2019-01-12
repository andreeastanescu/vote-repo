from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from vot.models import VotDigital


class FirstView(TemplateView):
    template_name="base.html"

class SecondView(ListView):
    template_name="vot/topic_list.html"
    queryset = VotDigital.objects.all()