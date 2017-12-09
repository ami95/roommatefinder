from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime.date(1989, 12, 25))
    GENDER_CHOICES = (('M', 'Male'), ('F','Female'), ('U', 'Unspecified'))
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default='Unspecified')
    city = models.CharField(max_length=100, default='Braşov')
    description = models.TextField()
    ocupation = models.CharField(max_length=100, default='Student')
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
                        ('U', 'Unspecified'))
    temperament = models.CharField(max_length=12, choices=TEMPERAMENT_CHOICES, default='Unspecified')
    is_smoker = models.BooleanField(default = False)
    has_pets = models.BooleanField(default = False)
    is_visible = models.BooleanField(default = False)
    image = models.ImageField(upload_to='profilepics', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
