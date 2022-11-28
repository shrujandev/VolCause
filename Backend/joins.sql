select M.Member_ID as Manager_ID,M.Name as Manager_Name ,
E.Event_ID as Event_ID ,E.Event_Name as Event_Name from 
MEMBERS_415 as M join Event_415 as E where m.Member_ID = E.Manager_ID;




--Volunteers of a perticular

select M.Member_ID as Member_ID,M.name as Name,M.gender as Gender from 
MEMBERS_415 as M join Volunteers_415 as V where V.Event_ID = "E22001" and M.Member_ID=V.Member_ID;


-- All manager and event details 

select E.event_name as Event_Name ,E.event_type as Event_Type ,E.event_date as Date ,M.Name as Manager_Name,
O.Org_Name as Organization from Event_415 as E join MEMBERS_415 as M On E.Manager_ID = M.Member_ID Join 
Organization_415 as O on E.Org_ID = O.Org_ID;


-- taking part in nothing 
select M.Member_ID as Member_ID,M.name as Name,M.gender as Gender from 
MEMBERS_415 as M where not exists (select * from Volunteers_415 as V where V.Member_ID=M.Member_ID);