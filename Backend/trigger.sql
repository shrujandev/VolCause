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



--Clashing dates
DELIMITER $$ 
create trigger clash_check
before insert on Volunteers_415 for each row
BEGIN
if(exists(select 1 from Event_415 E1,Event_415 E2 join volunteers_415 as V where v.member_id = new.member_id and v.event_id != new.event_id and v.event_id = E1.event_id and E2.event_id = new.event_id and E1.event_date = E2.event_date )) then
signal sqlstate '45000' set message_text ='Multiple Event signup on the same day is not allowed ';
end if;
end $$
DELIMITER ;