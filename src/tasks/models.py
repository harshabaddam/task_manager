from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    """
    This model maintains the details of all the tasks
    """
    STATUS_CHOICES = (
        ('to do', 'To Do'),
        ('in progress', 'In Progress'),
        ('done', 'Done')
    )
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    due_data = models.DateTimeField()
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assign', db_column='assignee', null=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='create', db_column='create_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='update', db_column='update_by')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'task'
        verbose_name_plural = 'Tasks'
