from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks import models, forms


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Create View for the TaskModel
    """
    model = models.TaskModel
    form_class = forms.TaskModelForm
    template_name = 'tasks/new.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update View for the TaskModel
    """
    model = models.TaskModel
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:list')
    pk_url_kwarg = 'id'
    fields = ['subject', 'description', 'status']

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete View for the TaskModel
    """
    model = models.TaskModel
    template_name = 'tasks/delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('tasks:list')

class TaskListView(LoginRequiredMixin, ListView):
    """
    This view is to display this list of all the tasks
    """
    model = models.TaskModel
    template_name = 'tasks/list.html'
