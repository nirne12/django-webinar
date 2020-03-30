from django.db import models

# Create your models here.

class complaint(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    RollNumber = models.CharField(max_length=25, null=True, blank=True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Date = models.DateField()

    def __str__(self):
        return self.Title + '(' + self.Name + ')'

