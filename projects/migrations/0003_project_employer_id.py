# Generated by Django 5.0.4 on 2024-04-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employer_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
