from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(max_length=30, blank=True)
    number_of_employer = models.CharField(max_length=30, blank=True)
    has_permission = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Students(models.Model):
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
    position = models.CharField(max_length=255, null=True)
    level = models.CharField(max_length=255, null=True)
    estimate_year_of_graduation = models.IntegerField(blank=True, null=True)
    specialisation = models.CharField(max_length=255, null=True, choices=SPECIALISATION)
    rating = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=100)

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return ""

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name='orders')
    product = models.ForeignKey(Students, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
