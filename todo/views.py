from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
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
    paginate_by = 5


def toggle_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.status:
        task.status = False
        task.save(update_fields=["status"])
    else:
        task.status = True
        task.save(update_fields=["status"])
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
