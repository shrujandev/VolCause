CREATE TABLE Event_Details_415(
    Event_Name varchar(255),
    Event_Type varchar(255),
    Event_Date date,
    Manager_Name varchar(255),
    Organization varchar(255)

);



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
