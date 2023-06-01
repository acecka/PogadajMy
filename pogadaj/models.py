# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# noinspection PyRedundantParentheses
WORKING_DAYS = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday')
)

# noinspection PyRedundantParentheses
SPECIALTIES = (
    ('Logopedia'),
    ('Terapia Metody Krakowskiej'),
    ('Neurologopedia'),
    ('Psychologia'),
    ('Terapia Integracji Sensorycznej')
)


class TherapistSpecialties(models.Model):
    specialty = models.CharField(max_length=128)
    description = models.TextField(max_length=512)


class ScheduleCalendar(models.Model):
    Schedule_hours = models.FloatField(
        default=9,
        validators=[MaxValueValidator(18.0), MinValueValidator(9.0)]
    )
    Schedule_days = models.CharField(choices=WORKING_DAYS)


class Therapist(models.Model):
    first_Name = models.CharField(max_length=64)
    last_Name = models.CharField(max_length=128)
    specialties = models.ManyToManyField(TherapistSpecialties)
    description = models.TextField()
    phone_Number = models.IntegerField
    emilAddress = models.EmailField()
    schedule = models.ManyToManyField(ScheduleCalendar)
    therapist_appointment = models.ManyToManyField('Client', through='Appointment')


class Client(models.Model):
    first_Name = models.CharField(max_length=64)
    last_Name = models.CharField(max_length=128)
    phone_Number = models.IntegerField
    emailAddress = models.EmailField()


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    visit_length = models.PositiveIntegerField()


class Link(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=256)
    email = models.EmailField()
    donation = models.CharField(max_length=1000)
