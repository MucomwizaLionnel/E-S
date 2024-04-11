# Generated by Django 3.2.12 on 2024-03-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_Chef_Equip',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Chefs',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Comptable',
        ),
        migrations.AddField(
            model_name='user',
            name='is_chef',
            field=models.BooleanField(default=False, verbose_name='Is chef'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_chef_Equip',
            field=models.BooleanField(default='True', verbose_name='Is chef d_equipe'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_comptable',
            field=models.BooleanField(default='False', verbose_name='Is comptable'),
        ),
    ]