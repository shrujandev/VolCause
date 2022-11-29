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





