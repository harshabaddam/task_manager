from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
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
    form_class = forms.TaskModelForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:list')
    pk_url_kwarg = 'id'

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

class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    This view is to display the details of a task
    """
    model = models.TaskModel
    template_name = 'tasks/detail.html'
    pk_url_kwarg = 'id'


@login_required
def update_status(request):
    """
    update the status of the task
    :return:
    """
    input_data = request.GET.copy()
    task = models.TaskModel.objects.get(id=input_data['id'])
    task.status = input_data['status']
    task.updated_by = request.user
    task.save()
    return JsonResponse({'status': input_data['status']})
