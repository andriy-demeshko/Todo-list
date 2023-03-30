# Generated by Django 4.1.5 on 2023-01-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("creation_date", models.DateTimeField()),
                ("deadline_date", models.DateTimeField()),
                ("status", models.BooleanField()),
                ("tags", models.ManyToManyField(related_name="tasks", to="todo.tag")),
            ],
            options={
                "ordering": ["status", "-creation_date"],
            },
        ),
    ]
