# Generated by Django 4.2 on 2024-01-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_students_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='study',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
