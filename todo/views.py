from django.views import generic
from .models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"

