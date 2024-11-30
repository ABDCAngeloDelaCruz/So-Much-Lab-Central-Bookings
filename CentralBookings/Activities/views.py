from django.shortcuts import render

# relative import of forms
from .models import Activity


def activities_view(request):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Activity.objects.all()
        
    return render(request, "activities.html", context)