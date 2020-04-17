from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

DATE_INPUT_FORMATS = ['%d-%m-%Y']

class Patient(models.Model):
	Name = models.CharField(max_length=150)
	IdentityDocumentNumber = models.CharField(max_length=50)
	DateOfBirth = models.DateField()
	DateCaseConfirmed = models.DateField()
	CaseNumber = models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class Location(models.Model):
	LocationVisited = models.CharField(max_length=150)
	Address = models.TextField(blank=True)
	District = models.CharField(max_length=150)
	XCoord = models.CharField(max_length=50)
	YCoord = models.CharField(max_length=50)
	DateFrom = models.DateField()
	DateTo = models.DateField()
	Detail = models.TextField(blank=True)
	Category = models.CharField(max_length=150)
	Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.LocationVisited} ({self.Patient})'
