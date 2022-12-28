from django.urls import reverse_lazy

from .models import Statement
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class StatementCreate(CreateView):
    model = Statement
    fields = '__all__'
    success_url = '/fillin/retrieves'


class StatementRetrieve(ListView):
    model = Statement
    success_url = reverse_lazy('statement: StatementRetrieve')


class StatementDetail(DetailView):
    model = Statement
    success_url = reverse_lazy('statement: StatementRetrieve')


class StatementUpdate(UpdateView):
    model = Statement
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/fillin/retrieves'

    # def get_success_url(self):


class StatementDelete(DeleteView):
    model = Statement
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/fillin/retrieves'
