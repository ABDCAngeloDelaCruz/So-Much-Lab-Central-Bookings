from django.db import connection
from django.shortcuts import render

# relative import of forms
from .models import Activity, Organizer, Participant, Booking, Department


def activities_list_view(request):
    cursor = connection.cursor()

    # Default query
    query = "SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, a.Start_Time, a.End_Time, a.Expected_Participants FROM organizer o, activity a WHERE o.Organizer_ID = a.Organizer_ID"

    # Added stuff based on user input

    # Single date
    filter_date = request.GET.get("filter_date")
    # Start of date range
    start_date = request.GET.get("start_date")
    # End of date range
    end_date = request.GET.get("end_date")
    # Organizer name
    organizer_name = request.GET.get("organizer")
    # Sort by category, default date but can be by Organizer
    sort_field = request.GET.get("sort_field", "a.Date")
    # Sort order, default ascending
    sort_order = request.GET.get("sort_order", "ASC")

    query_params = []

    if filter_date:
        query += " AND a.Date = %s"
        query_params.append(filter_date)
    elif start_date and end_date:
        query += " AND a.Date BETWEEN %s AND %s"
        query_params.extend([start_date, end_date])

    if organizer_name:
        query += " AND o.Organizer_Name = %s"
        query_params.append(organizer_name)

    if sort_field in ["a.Date", "o.Organizer_Name"] and sort_order.upper() in ["ASC", "DESC"]:
        query += f" ORDER BY {sort_field} {sort_order.upper()}"

    cursor.execute(query, query_params)
    query_results = cursor.fetchall()

    return render(request, "activities.html", {'data': query_results})


def organizer_info_list_view():
    return


def participant_activity_booking_list_view():
    return
