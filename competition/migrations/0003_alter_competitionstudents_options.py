# Generated by Django 4.2 on 2023-04-05 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_rename_students_competitionstudents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competitionstudents',
            options={'verbose_name': 'CompetitionStudent', 'verbose_name_plural': 'CompetitionStudents'},
        ),
    ]