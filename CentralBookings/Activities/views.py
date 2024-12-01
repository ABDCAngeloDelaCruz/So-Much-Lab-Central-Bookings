from django.db import connection
from django.shortcuts import render


from .models import Activity, Organizer


def home_view(request):
    return render(request, "home.html")


def activities_list_view(request):
    cursor = connection.cursor()

    query = "SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, a.Start_Time, a.End_Time, a.Expected_Participants FROM organizer o, activity a WHERE o.Organizer_ID = a.Organizer_ID"
    query_params = []

    if request.GET.get('reset') == 'true':
        filter_date = ''
        start_time = ''
        end_time = ''
        organizer_name = 'all'
        location_name = 'all'
        sort_field = 'a.Date'
        sort_order = 'ASC'
    else:
        filter_date = request.GET.get("filter_date")
        start_time = request.GET.get("start_time")
        end_time = request.GET.get("end_time")
        organizer_name = request.GET.get("organizer_field")
        location_name = request.GET.get("location_field")
        sort_field = request.GET.get("sort_field", "a.Date")
        sort_order = request.GET.get("sort_order", "ASC")

    if filter_date:
        query += " AND a.Date = %s"
        query_params.append(filter_date)

    if start_time:
        query += " AND a.Start_Time >= %s"
        query_params.append(start_time)

    if end_time:
        query += " AND a.End_Time <= %s"
        query_params.append(end_time)

    if organizer_name and organizer_name != "all":
        query += " AND o.Organizer_Name = %s"
        query_params.append(organizer_name)

    if location_name and location_name != "all":
        query += " AND a.Location = %s"
        query_params.append(location_name)

    if sort_field in ["o.Organizer_Name", "a.Activity_Name", "a.Location", "a.Date", "a.Start_Time", "a.End_Time"] and sort_order.upper() in ["ASC", "DESC"]:
        query += f" ORDER BY {sort_field} {sort_order.upper()}"

    cursor.execute(query, query_params)
    query_results = cursor.fetchall()

    organizers = Organizer.objects.all()
    locations = Activity.objects.all()

    return render(request, "activities.html", {'data': query_results, 'orgs': organizers, 'locs': locations, 'filter_date': filter_date, 'start_time': start_time, 'end_time': end_time, 'organizer_name': organizer_name, 'location_name': location_name, 'sort_field': sort_field, 'sort_order': sort_order})


def organizer_info_list_view(request):
    cursor = connection.cursor()

    cursor.execute("SELECT Organizer_Name FROM organizer")
    organizers = cursor.fetchall()

    selected_organizer = request.GET.get("organizer", None)

    organizer_details = None
    activities = []

    organizer_query = "SELECT Organizer_ID, Organizer_Name, Contact_Person_Given_Name, Contact_Person_Middle_Initial, Contact_Person_Last_Name, Contact_Email, Contact_Number, Organizer_Type, Organizer_Address FROM organizer WHERE Organizer_Name = %s"
    activities_query = "SELECT a.Activity_Name, a.Location, a.Date, a.Start_Time, a.End_Time FROM activity a, organizer o WHERE a.Organizer_ID = o.Organizer_ID AND o.Organizer_Name = %s"

    if selected_organizer:
        cursor.execute(organizer_query, [selected_organizer])
        organizer_details = cursor.fetchone()

        if organizer_details:
            organizer_details = (
                f"{int(organizer_details[0]):05d}", *organizer_details[1:])

        cursor.execute(activities_query, [selected_organizer])
        activities = cursor.fetchall()

    return render(request, "organizer-info.html", {"organizers": organizers,
                                                   "selected_organizer": selected_organizer,
                                                   "organizer_details": organizer_details,
                                                   "activities": activities, }
                  )


def participant_booking_view(request):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            ID_Number, 
            CONCAT(Participant_Given_Name, ' ', 
                   COALESCE(Participant_Middle_Initial || '. ', ''), 
                   Participant_Last_Name) AS Participant_Name 
        FROM participant
    """)
    participants = cursor.fetchall()

    participant_id = request.GET.get("participant_id", None)
    booking_details = []
    data = []

    if participant_id:
        query = """
            SELECT 
                CONCAT(p.Participant_Given_Name, ' ', 
                       COALESCE(p.Participant_Middle_Initial || '. ', ''), 
                       p.Participant_Last_Name) AS Participant_Name,
                p.Birth_Date,
                d.Department_Name,
                p.Participant_Type,
                b.Participant_ID,
                o.Organizer_Name,
                a.Activity_Name,
                a.Date,
                a.Location,
                a.Start_Time,
                a.End_Time,
                b.Has_Attended
            FROM 
                participant p, department d, booking b, activity a, organizer o
            WHERE
                p.Department_ID = d.Department_ID
            AND 
                p.ID_Number = b.Participant_ID
            AND 
                b.Activity_ID = a.Activity_ID
            AND 
                a.Organizer_ID = o.Organizer_ID               
            AND 
                p.ID_Number = %s
        """
        cursor.execute(query, [participant_id])
        booking_details = cursor.fetchall()

        data = [
            {
                "participant_name": row[0],
                "birth_date": row[1],
                "department_name": row[2],
                "participant_type": row[3],
                "id_number": f"{row[4]:05}",
                "organizer_name": row[5],
                "activity_name": row[6],
                "activity_date": row[7],
                "location": row[8],
                "start_time": row[9],
                "end_time": row[10],
                "attended": row[11],
            }
            for row in booking_details
        ]

    return render(request, "participant-booking.html", {
        "participants": participants,
        "data": data,
        "selected_participant_id": participant_id,
    })
