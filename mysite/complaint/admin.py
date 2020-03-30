from django.contrib import admin
from .models import Complaint

# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    class Meta :
        model = Complaint
