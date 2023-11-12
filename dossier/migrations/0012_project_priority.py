# Generated by Django 4.2.7 on 2023-11-12 00:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dossier", "0011_post_creator_post_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="priority",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
