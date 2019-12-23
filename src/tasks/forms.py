from .models import TaskModel
from django.forms import ModelForm


class TaskModelForm(ModelForm):
    """
    Model form for TaskModel
    """
    class Meta:
        model = TaskModel
        exclude = ['id', 'created_by', 'created_date', 'updated_by', 'updated_date']

