-- CREATE DATABASE cenbookdb;

-- \c cenbookdb

CREATE TABLE organizer (
	Organizer_ID SERIAL PRIMARY KEY,
    Organizer_Name VARCHAR(255) NOT NULL,
    Organizer_Type VARCHAR(50) NOT NULL CHECK (Organizer_Type IN ('Internal', 'External')),
    Organizer_Address VARCHAR(255) NOT NULL,
    Contact_Person_Given_Name VARCHAR(255) NOT NULL,
    Contact_Person_Middle_Initial VARCHAR(255),
    Contact_Person_Last_Name VARCHAR(255) NOT NULL,
    Contact_Email VARCHAR(100) NOT NULL,
    Contact_Number VARCHAR(50) NOT NULL
);

CREATE TABLE activity (
    Activity_ID SERIAL PRIMARY KEY,
    Activity_Name VARCHAR(255) NOT NULL,
    Date DATE NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Start_Time TIME NOT NULL,
    End_Time TIME NOT NULL,
    Expected_Participants INT NOT NULL,
    Organizer_ID INT,
	FOREIGN KEY (Organizer_ID) REFERENCES organizer(Organizer_ID),
	CONSTRAINT unique_time_location UNIQUE (Date, Start_Time, End_Time, Location)
);

CREATE TABLE department (
    Department_ID SERIAL PRIMARY KEY,
    Department_Name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE participant (
    ID_Number SERIAL PRIMARY KEY,
    Participant_Given_Name VARCHAR(255) NOT NULL,
    Participant_Middle_Initial VARCHAR(255),
    Participant_Last_Name VARCHAR(255) NOT NULL,
    Birth_Date DATE NOT NULL,
    Participant_Type VARCHAR(50) NOT NULL CHECK (Participant_Type IN ('Student', 'Faculty', 'Staff Member')),
    Department_ID INT,
	FOREIGN KEY (Department_ID) REFERENCES department(Department_ID)
);

CREATE TABLE booking (
    Booking_No SERIAL PRIMARY KEY,
    Activity_ID INT,
    Participant_ID INT,
	FOREIGN KEY (Activity_ID) REFERENCES activity(Activity_ID),
	FOREIGN KEY (Participant_ID) REFERENCES participant(ID_Number),
    Has_Attended VARCHAR(5) NOT NULL CHECK(Has_Attended IN ('YES', 'NO')) DEFAULT 'NO'
);


-- INSERT INTO organizer (Organizer_Name, Organizer_Type, Organizer_Address, Contact_Person_Given_Name, Contact_Person_Middle_Initial, Contact_Person_Last_Name,
-- Contact_Email, Contact_Number)
-- VALUES ('TechEx Organizers', 'Internal', 'Katipunan, Quezon City', 'Harith', 'D', 'Magiba', 't1@gmail.com', '09092200909'),
--        ('Earth is Love Organization', 'External', 'Barangka, Marikina', 'Feli', 'Z', 'Navidad', 'mrbeast@yahoo.com', '09998883856'),
--        ('Math Workshop Organizers', 'Internal', 'Tondo, Manila', 'Gusion', null, 'Delos Santos', 'teamsecret@gmail.com', '09998881234'),
--        ('Chinese For Everyone', 'External', 'Binondo, Manila', 'Alice', null, 'Calugay', 'aguo@pogo.com', '09355541234'),
--        ('Engineers and Innovators', 'External', 'Poblacion, Makati', 'Bill', null, 'Zuckerburg', 'bz@tech.com', '09678889209'),
--        ('Bio is Life', 'Internal', 'Katipunan, Quezon City', 'Charles', 'H', 'Dawin', 'cdawin@gmail.com', '09448731309'),
--        ('Humanities Lovers', 'Internal', 'Katipunan, Quezon City', 'Michelle', null, 'Reyes-Guo', 'mreyes@gmail.com', '09355364234'),
--        ('Scholars Hub', 'Internal', 'Katipunan, Quezon City', 'Reg', 'I', 'Strar', 'regstrar@gmail.com', '09357824599');

-- INSERT INTO activity (Activity_Name, Date, Location, Start_Time, End_Time, Expected_Participants, Organizer_ID)
-- VALUES ('Tech Conference', '2023-11-01', 'Convention Center', '09:00:00', '17:00:00', 50, 1),
--        ('LaTeX for Dummies', '2023-11-02', 'Room A', '14:00:00', '16:00:00', 30, 3),
--        ('Blockchain 101', '2023-11-02', 'Room C', '14:00:00', '16:00:00', 20, 1),
--        ('Basics of Building a Bridge', '2023-11-02', 'SEC B - 213', '14:00:00', '16:00:00', 15, 5),
--        ('How to Become a Cloud Engineer in 60 Days', '2023-11-02', 'New Rizal Library 5th Floor', '14:00:00', '16:00:00', 40, 1),
--        ('Acting Workshop','2023-11-03', 'Covered Courts', '15:00:00', '17:00:00', 10, 7),
--        ('How to Protect Our Planet','2023-11-05', 'Faura', '13:00:00', '15:00:00', 30, 2),
--        ('Microplastics in our Body','2023-11-05', 'SEC B - 113', '13:00:00', '15:00:00', 20, 6),
--        ('Chinese Language and Culture Workshop', '2024-12-09', 'SOM 305', '10:00:00', '12:30:00', 30, 4),
--        ('Philosophy Symposium', '2023-12-11', 'Humanities Center', '13:30:00', '16:30:00', 45, 7),
--        ('Fundamentals of Computer Vision', '2023-12-7', 'Faura AVR', '8:30:00', '17:30:00', 18, 1);
       
 
-- INSERT INTO department (Department_Name)
-- VALUES ('Computer Science'),
--        ('Mathematics'),
--        ('Biology'),
--        ('Engineering'),
--        ('Environmental Science'),
--        ('Chinese Studies'),
-- 	   ('Humanities');

-- INSERT INTO participant (Participant_Given_Name, Participant_Middle_Initial, Participant_Last_Name, Birth_Date, Participant_Type, Department_ID)
-- VALUES ('Juan', 'B', 'Dela Cruz', '1990-05-15', 'Student', 1),
--        ('Faker', 'M', 'Santos', '1985-03-20', 'Faculty', 1),
--        ('Charles', 'P', 'Leclerc', '1995-07-10', 'Staff Member', 2),
--        ('Lewis', null, 'Hamilton', '1985-01-07', 'Faculty', 3),
--        ('Wanwan', 'A', 'Reyes', '2003-08-15', 'Student', 7),
--        ('Tigreal', 'M', 'Guadalupe', '2002-06-15', 'Student', 5),
--        ('Grock', NULL, 'Sy', '1985-09-20', 'Faculty', 4),
--        ('Cathy', 'L', 'Brown', '1995-03-12', 'Staff Member', 6),
--        ('Hylos', 'R', 'Garcia', '1990-11-10', 'Faculty', 7),
--        ('Emily', NULL, 'Davis', '2000-04-05', 'Student', 2);
 
-- INSERT INTO booking (Activity_ID, Participant_ID, Has_Attended)
-- VALUES (1, 1, 'YES'),
--        (1, 2, 'YES'),
--        (1, 3, 'YES'),
--        (1, 10, 'NO'),
--        (2, 3, 'YES'),
--        (2, 8, 'YES'),
--        (2, 4, 'NO'),
-- 	   (4, 5, 'YES'),
--        (1, 4, 'NO'),
--        (6, 3, 'YES'),
--        (4, 10, 'YES'),
-- 	   (10, 1, 'NO'),
--        (8, 2, 'YES'),
--        (5, 3, 'YES'),
--        (7, 10, 'NO'),
-- 	   (7, 1, 'YES'),
--        (5, 2, 'YES'),
--        (4, 7, 'NO'),
--        (11, 10, 'YES');

-- SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, 
-- a.Start_Time, a.End_Time, a.Expected_Participants 
-- FROM organizer o, activity a 
-- WHERE o.Organizer_ID = a.Organizer_ID 
-- ORDER BY a.Date ASC;

-- SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, 
-- a.Start_Time, a.End_Time, a.Expected_Participants 
-- FROM organizer o, activity a 
-- WHERE o.Organizer_ID = a.Organizer_ID AND a.Date = '2023-11-02' 
-- ORDER BY a.Date ASC;

-- SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, 
-- a.Start_Time, a.End_Time, a.Expected_Participants 
-- FROM organizer o, activity a 
-- WHERE o.Organizer_ID = a.Organizer_ID AND a.Date = '2023-11-05' 
-- ORDER BY o.Organizer_Name DESC;

-- SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, 
-- a.Start_Time, a.End_Time, a.Expected_Participants 
-- FROM organizer o, activity a 
-- WHERE o.Organizer_ID = a.Organizer_ID AND o.Organizer_Name = 'TechEx Organizers' 
-- ORDER BY a.Date DESC;

-- SELECT o.Organizer_Name, a.Activity_Name, a.Location, a.Date, 
-- a.Start_Time, a.End_Time, a.Expected_Participants 
-- FROM organizer o, activity a 
-- WHERE o.Organizer_ID = a.Organizer_ID AND a.Start_Time >= '10:00' AND a.End_Time <= '16:00' 
-- ORDER BY a.Date ASC;