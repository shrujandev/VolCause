DROP DATABASE VOLCAUSE_415;
CREATE DATABASE VOLCAUSE_415;

USE VOLCAUSE;

CREATE TABLE MEMBERS_415(
    Member_ID int not null,
    Name varchar(255),
    Gender varchar(255),
    DOB date,
    Age int,
    Blood_group varchar(255),
    Address varchar(255),
    
    PRIMARY KEY (Member_ID)

);


CREATE TABLE CONTACT_415(
    Member_ID int not null,
    Phone varchar(10),
    
    CONSTRAINT chk_phone CHECK (phone not like '%[^0-9]%'), 
    FOREIGN KEY(Member_ID) REFERENCES MEMBERS_415(Member_ID) on DELETE CASCADE

);

CREATE TABLE ORGANIZATION_415(
    Org_ID varchar(255) not null,
    Org_Name varchar(255),
    Org_Manager varchar(255),

    PRIMARY KEY (Org_ID)
);

CREATE TABLE Event_415(
    Event_ID VARCHAR(255) not null,
    Event_Name varchar(255) not null,
    Manager_ID int not null,
    Event_Type varchar(255),
    Event_Date DATE not null,
    Event_Time TIME,
    Venue varchar(255),
    Volunteer_count int,
    Org_ID VARCHAR(255) not null,

    PRIMARY KEY (Event_ID),
    FOREIGN KEY(Manager_ID) REFERENCES MEMBERS_415(Member_ID) on DELETE CASCADE,
    FOREIGN KEY(Org_ID) REFERENCES ORGANIZATION_415(Org_ID) on DELETE CASCADE
    

);

CREATE TABLE Manager_415(
    Manager_ID int not null,
    Manager_Name varchar(255),
    Event_ID varchar(255) not null,
    Event_Name varchar(255),

    PRIMARY KEY (Manager_ID,Event_ID),
    FOREIGN KEY(Manager_ID) REFERENCES MEMBERS_415(Member_ID) on DELETE CASCADE,
    FOREIGN KEY(Event_ID) REFERENCES Event_415(Event_ID) on DELETE CASCADE

);


CREATE TABLE Volunteers_415(
    Event_ID varchar(255) not null,
    Member_ID int not null,

    FOREIGN KEY(Event_ID) REFERENCES Event_415(Event_ID) on DELETE CASCADE,
    FOREIGN KEY(Member_ID) REFERENCES MEMBERS_415(Member_ID) on DELETE CASCADE

);

