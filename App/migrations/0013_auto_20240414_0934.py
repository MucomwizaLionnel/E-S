# Generated by Django 3.2.12 on 2024-04-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20240409_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tache',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tache',
            name='technicien',
        ),
        migrations.AddField(
            model_name='tache',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
