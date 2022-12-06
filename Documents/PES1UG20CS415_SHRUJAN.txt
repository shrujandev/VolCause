--PES1UG20CS415
--SHRUJAN

--DDL 

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




-------------------------------------Joins----------------------------------------------

--manager and event details
select M.Member_ID as Manager_ID,M.Name as Manager_Name ,
E.Event_ID as Event_ID ,E.Event_Name as Event_Name from 
MEMBERS_415 as M join Event_415 as E where m.Member_ID = E.Manager_ID;



--Volunteers of a perticular event
select M.Member_ID as Member_ID,M.name as Name,M.gender as Gender from 
MEMBERS_415 as M join Volunteers_415 as V where V.Event_ID = "E22001" 
and M.Member_ID=V.Member_ID;


-- All manager,organisation and event details
select E.event_name as Event_Name ,E.event_type as Event_Type ,E.event_date as Date ,M.Name as Manager_Name,
O.Org_Name as Organization from Event_415 as E join MEMBERS_415 as M On E.Manager_ID = M.Member_ID Join 
Organization_415 as O on E.Org_ID = O.Org_ID;


-- member taking part in nothing 
select M.Member_ID as Member_ID,M.name as Name,M.gender as Gender from 
MEMBERS_415 as M where not exists (select * from Volunteers_415 as V 
where V.Member_ID=M.Member_ID);


-------------------------------------------Aggregate ---------------------------------------

--No of volunteers in the event 
select E.Event_Name as Event_Name, count(V.Member_ID) as Number_of_Volunteers
from Event_415 as E join Volunteers_415 as V 
on E.Event_ID = V.Event_ID group by(V.Event_ID);


--event per manager
select M.Manager_Name as Manager_Name,count(M.Event_ID) as Events 
from Manager_415 as M group by (Manager_ID);


--Event per volunteer 
select M.Member_Id as Member_ID,M.name as Name,count(E.event_ID) as Number_of_Events 
from Members_415 as M left join Volunteers_415 as E on m.Member_ID = E.Member_ID group by (M.Member_ID);


--Number of event in a day
select E.event_date as Date , count(e.event_id) as Number_of_events 
from Event_415 as E group by (e.event_date);


--------------------------------------SET Operations --------------------------------------------
--org and event
select Org_Manager,Org_Name from ORGANIZATION_415
Union
select Event_Name,Event_Type from Event_415;

--org and event union all
select Org_ID,Org_Manager,Org_Name from ORGANIZATION_415
Union all
select Event_ID,Event_Name,Event_Type from Event_415;


--members who are volunteers
select distinct Member_ID from Volunteers_415 
intersect 
select Member_ID from MEMBERS_415;

--members who are not managers
select Member_ID from MEMBERS_415
except
select Manager_ID from Manager_415;





---------------------------Functions and Procedure------------------------------------------------------

--Function to calculate Number of days till the start of the event 
DELIMITER $$
create function days_till_event(event_date date)
returns int 
deterministic
BEGIN
declare date2 date;
select current_date() into date2;
return DATEDIFF(event_date,date2);
end $$
DELIMITER ;


--Prcedure to calculate the age 
DELIMITER $$
CREATE PROCEDURE getAge()
BEGIN
UPDATE Members_415 SET Age= DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), dob)), '%Y') + 0;
END;$$
DELIMITER ;



--Procedure to calculate the number of volunteers
DELIMITER $$
CREATE PROCEDUre setVol()
BEGIN
DROP table if exists T2;
Create Table T2 as (select Event_415.event_id as EID,count(Volunteers_415.Member_ID) 
as countVal from Event_415 join Volunteers_415 on Event_415.Event_ID = Volunteers_415.Event_ID 
group by(Volunteers_415.Event_ID));
UPDATE Event_415 join T2 on Event_415.Event_ID = T2.EID 
SET Event_415.Volunteer_Count = T2.countval ;
Drop table T2;
END;$$
DELIMITER ;



---------------------------------------Triggers and cursors --------------------------------------

--Trigger to restrict age 
DELIMITER $$
create trigger age_check
before insert on Members_415 for each row
BEGIN
if(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), new.dob)), '%Y') < 18) then
signal sqlstate '45000' set message_text ='Age is less than 18 Years ';
end if;
if (DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), new.dob)), '%Y') > 65) then
signal sqlstate '45000' set message_text ='Age is greater than 65 ';
end if;
end $$
DELIMITER ;



--Trigger to prevet Clashing dates
DELIMITER $$ 
create trigger clash_check
before insert on Volunteers_415 for each row
BEGIN
if(exists(select 1 from Event_415 E1,Event_415 E2 join volunteers_415 as V
where v.member_id = new.member_id and v.event_id != new.event_id 
and v.event_id = E1.event_id and E2.event_id = new.event_id and E1.event_date = E2.event_date )) then
signal sqlstate '45000' set message_text ='Multiple Event signup on the same day is not allowed ';
end if;
end $$
DELIMITER ;



--Cursor to create a backup table for event details

DELIMITER $$
create procedure createEventDet()
BEGIN
drop table if exists Event_Details_415;
CREATE TABLE Event_Details_415(
    Event_Name varchar(255),
    Event_Type varchar(255),
    Event_Date date,
    Manager_Name varchar(255),
    Organization varchar(255)

);
END;$$
DELIMITER ; 
DELIMITER $$


create PROCEDURE event_details()
BEGIN
declare done int default 0;
declare Event_Name varchar(255);
declare Event_Type varchar(255);
declare Manager_Name varchar(255);
declare Organization varchar(255);
declare Event_date date;
declare cur Cursor for (select E.event_name as Event_Name ,E.event_type as Event_Type ,E.event_date as Date ,M.Name as Manager_Name,
O.Org_Name as Organization from Event_415 as E join MEMBERS_415 as M On E.Manager_ID = M.Member_ID Join 
Organization_415 as O on E.Org_ID = O.Org_ID);
Declare CONTINUE HANDLER FOR NOT FOUND SET done = 1;
call createEventDet();
OPEN cur;
label:LOOP

FETCH cur INTO Event_Name,Event_Type,Event_Date,Manager_Name,Organization;
INSERT into Event_details_415 value(Event_Name,Event_Type,Event_Date,Manager_Name,Organization);
IF done =1 Then leave label;
end if;
end loop;
close cur;
select * from Event_Details_415;

end $$
DELIMITER ;