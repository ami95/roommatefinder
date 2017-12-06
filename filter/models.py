from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

class Ocupation(models.Model):
    name = models.CharField(max_length=100, default='Student')
    field = models.CharField(max_length=100, default='Informatics')

    class Meta:
        verbose_name = 'Ocupation'
        verbose_name_plural = 'Ocupations'
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, default='Braşov')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.ForeignKey('auth.User')
    dob = models.DateField(default=datetime.date(1989, 12, 25))
    GENDER_CHOICES = (('M', 'Male'), ('F','Female'), ('U', 'Unspecified'))
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default='U')
    city = models.ForeignKey('City')
    description = models.TextField()
    ocupation = models.ForeignKey('Ocupation')
    monthly_budget = models.IntegerField(default=500, validators=[
                                                        MaxValueValidator(10000),
                                                        MinValueValidator(1)])
    tidyness_lvl = models.IntegerField(default=50, validators=[
                                                        MaxValueValidator(100),
                                                        MinValueValidator(1)])
    guests_lvl = models.IntegerField(default=50, validators=[
                                                        MaxValueValidator(100),
                                                        MinValueValidator(1)])
    TEMPERAMENT_CHOICES = (('S', 'Sanguine'), ('P', 'Phlegmatic'),
                        ('C', 'Choleric'), ('M', 'Melancholic'),
                        ('I', 'Irelevant'))
    temperament = models.CharField(max_length=12, choices=TEMPERAMENT_CHOICES, default='I')
    is_smoker = models.BooleanField()
    has_pets = models.BooleanField()
    is_visible = models.BooleanField()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['author']

        def __str__(self):
            return self.name

class PotentialRoommates(models.Model):
    potential_roommate = models.ForeignKey('Profile')

    def __str__(self):
        return self.name
