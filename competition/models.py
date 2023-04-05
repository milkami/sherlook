from django.db import models
from apps.accounts.models import *


# Create your models here.
class Competitions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True)
    year = models.IntegerField(default=0)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ""

    class Meta:
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255, null=True)
    university = models.CharField(max_length=255, null=True)
    competition = models.ForeignKey(
        Competitions, on_delete=models.CASCADE, db_column='competition_id',
        related_name='teams', blank=True, null=True
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ""

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class CompetitionStudents(models.Model):
    SPECIALISATION = (
        ('Team Captain', 'Team Captain'),
        ('Chief Engineer', 'Chief Engineer'),
        ('Aerodynamics', 'Aerodynamics'),
        ('Powertrain', 'Powertrain'),
        ('Chassis', 'Chassis'),
        ('Engine', 'Engine'),
        ('Electronics & Wiring', 'Electronics & Wiring'),
        ('Suspension', 'Suspension'),
        ('IT', 'IT'),
        ('Team Member', 'Team Member'),
        ('Manufacturing', 'Manufacturing'),

    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, null=True)
    mobile_phone_number = models.CharField(max_length=255, null=True)
    nationality = models.CharField(max_length=255, null=True)
    study = models.CharField(max_length=255, null=True)
    level = models.CharField(max_length=255, null=True)
    estimate_year_of_graduation = models.IntegerField(default=None)
    role_in_the_team = models.CharField(max_length=255, null=True, choices=SPECIALISATION)
    role_at_the_competition = models.CharField(max_length=255, null=True)
    team = models.ForeignKey(
        Teams, on_delete=models.CASCADE, db_column='team_id',
        related_name='students', blank=True, null=True
    )
    student = models.ForeignKey(
        Students, on_delete=models.CASCADE, db_column='student_id',
        related_name='competition_students', blank=True, null=True
    )
    status = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ""

    class Meta:
        verbose_name = 'CompetitionStudent'
        verbose_name_plural = 'CompetitionStudents'
