# Eagle Hill College Central Bookings

This is a group project for the Information Management class where we created an application which allows users from Eagle Hill College to check out the Organizers of Activities, the Activities that users have booked, and the list of Activities that are available.

## How to Run

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository into your working machine.
2. Make sure that you have [Python](https://www.python.org/downloads/) installed in your machine. It is recommended to use Python 3.
3. Make sure that you have [PostgreSQL](https://www.postgresql.org/download/) installed in your machine.
4. Setup a virtual environment for your working directory which must contain this project that was cloned from remote.
5. Make sure you're in the same directory where the `requirements.txt` is. Run the following in your command line:

```bash
pip install -r requirements.txt
```

5. Change your working directory to `CentralBookings/`
6. Run the following command. Enter the password that you set.

```bash
psql -U postgres
```

> **Note**: This is under the assumption that when you set up PostgreSQL, you had a user named `postgres`. If you set up another user, you can use that as well.

6. Run the following command to populate the database. Exit `psql` afterwards.

```pgsql
\i cbpostgres.sql
```

7. Run the following commands:

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

8. Go to `http://127.0.0.1:8000/`

## How to Use

1. In the Home tab, you can see some information on what Central Bookings is all about.
2. In the Organizer Information tab, you can select an organizer that you want to check. Their information as well as the activities that they have in store will be shown.
3. In the Activities List tab, you can find a list of activities based on the filters that you set.
4. In the Activity Booking Summary tab, you can choose any Participant. You will be shown their information as well as their schedule of activities.


Enjoy!

## Credits

Much thanks to [James](https://github.com/kintengg), [Dustin](https://github.com/DustinAgner27), [Gelo](https://github.com/angelo-dlcrz), and [Cyril](https://github.com/CyrilCDL) for making this happen!
