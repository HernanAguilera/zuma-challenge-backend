from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Number
from .forms import NumberForm

__all__ = ('NumberList', 'NumberCreate', 'NumberDetail')

SUCCESS_URL = reverse_lazy('index')

class NumberList(ListView):
    model = Number
    context_object_name = 'elements'
    template_name='numeros/list.html'

class NumberCreate(CreateView):
    model = Number
    form_class = NumberForm
    success_url = SUCCESS_URL
    template_name = "numeros/create.html"

class NumberDetail(DetailView):
    model = Number
    template_name='numeros/show.html'


class NumberUpdate(UpdateView):
    model = Number
    form_class = NumberForm
    success_url = SUCCESS_URL
    template_name = "numeros/update.html"


class NumberDeleteView(DeleteView):
    model = Number
    success_url = SUCCESS_URL
    template_name = "numeros/delete.html"
