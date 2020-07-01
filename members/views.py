from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from members.models import Members

class ListMembers(ListView):
    template_name = 'list_members.html'
    model = Members

class AddMembers(CreateView):
    template_name = 'members_form.html'
    model = Members
    fields = ['memberid', 'membername', 'contribution']
    success_url = reverse_lazy('list_members')

class EditMembers(UpdateView):
    template_name = 'members_form.html'
    model = Members
    fields = ['memberid', 'membername', 'contribution']
    success_url = reverse_lazy('list_members')

class DeleteMembers(DeleteView):
    template_name = 'members_confirm_delete.html'
    model = Members
    success_url = reverse_lazy('list_members')


# Create your views here.
