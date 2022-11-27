select M.Member_ID as Manager_ID,M.Name as Manager_Name ,
E.Event_ID as Event_ID ,E.Event_Name as Event_Name from 
MEMBERS_415 as M join Event_415 as E where m.Member_ID = E.Manager_ID;





select 