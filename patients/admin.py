from django.contrib import admin

# Register your models here.

from .models import Patients,Patients_mood

class PatientsAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'email') 

class Patients_moodAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('mood', 'emotions') 

# Basic registration
admin.site.register(Patients,PatientsAdmin)
admin.site.register(Patients_mood,Patients_moodAdmin)
