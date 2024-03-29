# Generated by Django 4.1.5 on 2023-01-31 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_task_deadline_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["status", "-created"]},
        ),
        migrations.RenameField(
            model_name="task",
            old_name="creation_date",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="deadline_date",
            new_name="deadline",
        ),
    ]
