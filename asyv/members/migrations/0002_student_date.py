# Generated by Django 4.2.4 on 2023-08-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
    ]
