from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField()
    deadline_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-creation_date"]

    def __str__(self):
        return f"{self.content} Create: {self.creation_date} Deadline: {self.deadline_date} status: {self.status}"
