# Generated by Django 4.2 on 2023-04-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_students_estimate_year_of_graduation'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='price',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
    ]
