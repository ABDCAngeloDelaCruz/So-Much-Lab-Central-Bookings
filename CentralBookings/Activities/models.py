# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         db_table = 'django_session'