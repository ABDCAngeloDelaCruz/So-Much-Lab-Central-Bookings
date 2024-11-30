from django.db import connection
from django.shortcuts import render

# relative import of forms
from .models import Activity, Organizer, Participant, Booking, Department


def activities_list_view(request):
    cursor = connection.cursor()
    #
    # query = "SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, a.Start_Time, a.End_Time, a.Expected_Participants FROM organizer o, activity a WHERE o.Organizer_ID = a.Organizer_ID"
    # filter_date = 
    #
    cursor.execute("SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, a.Start_Time, a.End_Time, a.Expected_Participants FROM organizer o, activity a WHERE o.Organizer_ID = a.Organizer_ID;")
    query = cursor.fetchall()
        
    return render(request, "activities.html", {'data': query})

def organizer_info_list_view():
    return

def participant_activity_booking_list_view():
    return