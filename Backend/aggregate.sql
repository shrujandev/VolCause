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




select avg(age) as Average_Age from Members_415;
select min(Volunteer_count) as Minimum_Number_Volunteers from Event_415;
select max(age) as Maximum_Age from Members_415;