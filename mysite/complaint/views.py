from django.shortcuts import render
from .forms import CreateComplaintForm
from django.http import HttpResponse

# Create your views here.

# Function based views

def create_complaint(request):
    new_complaint = CreateComplaintForm
    if request.method == 'POST':
        new_complaint = CreateComplaintForm(request.POST)
        if new_complaint.is_valid():
            new_complaint.save()
            return HttpResponse("Complaint Registered")
        else:
            return HttpResponse("Incorrect Format")

    return render(request, "complaint/create-complaint.html" , {'form': CreateComplaintForm})