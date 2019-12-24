"""URL patterns for tasks application"""
from django.urls import path
from tasks import views

app_name = 'tasks'
urlpatterns = [
    path('new/', views.TaskCreateView.as_view(), name='new'),
    path('list/', views.TaskListView.as_view(), name='list'),
    path('update/<int:id>', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:id>', views.TaskDeleteView.as_view(), name='delete'),
    path('view/<int:id>', views.TaskDetailView.as_view(), name='view'),
    path('update_status', views.update_status, name='update_status')
]