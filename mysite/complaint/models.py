from django.db import models

# Create your models here.

class Complaint(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    RollNumber = models.CharField(max_length=25, null=True, blank=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Date = models.DateField()

    def __str__(self):
        return self.Title

