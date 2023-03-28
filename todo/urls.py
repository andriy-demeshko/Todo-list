from django.urls import path

from .views import TaskListView, TagListView, toggle_task_status

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("toggle-status/<int:pk>", toggle_task_status, name="toggle-task-status")
]

app_name = "todo"
