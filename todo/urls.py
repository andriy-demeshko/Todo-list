from django.urls import path

from .views import (TaskListView, TagListView, ToggleTaskStatus,
                    TagCreateView, TagUpdateView, TagDeleteView,
                    TaskCreateView, TaskUpdateView, TaskDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("toggle-status/<int:pk>/", ToggleTaskStatus.as_view(),
         name="toggle-task-status"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo"
