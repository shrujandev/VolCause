--org and event
select Org_Manager,Org_Name from ORGANIZATION_415
Union
select Event_Name,Event_Type from Event_415;


select Org_ID,Org_Manager,Org_Name from ORGANIZATION_415
Union all
select Event_ID,Event_Name,Event_Type from Event_415;


select distinct Member_ID from Volunteers_415 
intersect 
select Member_ID from MEMBERS_415;


select Member_ID from MEMBERS_415
except
select Manager_ID from Manager_415;