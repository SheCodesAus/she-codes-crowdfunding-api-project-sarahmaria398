# Generated by Django 4.0.2 on 2022-08-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.IntegerField(),
        ),
    ]