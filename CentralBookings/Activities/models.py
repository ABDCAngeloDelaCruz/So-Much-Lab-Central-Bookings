from django.db import models


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    expected_participants = models.IntegerField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'activity'
        unique_together = (('date', 'start_time', 'end_time', 'location'),)


class Booking(models.Model):
    booking_no = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    participant = models.ForeignKey('Participant', models.DO_NOTHING, blank=True, null=True)
    has_attended = models.CharField(max_length=5)

    class Meta:
        db_table = 'booking'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'department'


class Organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True)
    organizer_name = models.CharField(max_length=255)
    organizer_type = models.CharField(max_length=50)
    organizer_address = models.CharField(max_length=255)
    contact_person_given_name = models.CharField(max_length=255)
    contact_person_middle_initial = models.CharField(max_length=255, blank=True, null=True)
    contact_person_last_name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)

    class Meta:
        db_table = 'organizer'


class Participant(models.Model):
    id_number = models.AutoField(primary_key=True)
    participant_given_name = models.CharField(max_length=255)
    participant_middle_initial = models.CharField(max_length=255, blank=True, null=True)
    participant_last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    participant_type = models.CharField(max_length=50)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'participant'