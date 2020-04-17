from django.contrib import admin
from .models import Patient
from .models import Location

admin.site.register(Patient)
admin.site.register(Location)