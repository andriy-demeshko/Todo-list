# Generated by Django 4.1.5 on 2023-01-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
