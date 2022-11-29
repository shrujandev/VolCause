DELIMITER $$
CREATE PROCEDURE getAge()
BEGIN
UPDATE Members_415 SET Age= DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), dob)), '%Y') + 0;
END;$$
DELIMITER ;




DELIMITER $$
CREATE PROCEDUre setVol()
BEGIN
DROP table if exists T2;
Create Table T2 as (select Event_415.event_id as EID,count(Volunteers_415.Member_ID) 
as countVal from Event_415 join Volunteers_415 on Event_415.Event_ID = Volunteers_415.Event_ID 
group by(Volunteers_415.Event_ID));
UPDATE Event_415 join T2 on Event_415.Event_ID = T2.EID SET Event_415.Volunteer_Count = T2.countval ;
Drop table T2;
END;$$
DELIMITER ;




