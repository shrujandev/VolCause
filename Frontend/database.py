import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="")
c = mydb.cursor()
c.execute("USE volcause_415")


def create_table():
    c.execute('CREATE table if not exists members_415 (Member_ID int not null,Name varchar(255),Gender varchar(255),DOB date,Age int,Blood_group varchar(255),Address varchar(255),PRIMARY KEY (Member_ID));')


def add_data(memberID, name, gender, dob, blood, address):
    c.execute('INSERT INTO members_415(Member_ID,Name,Gender,DOB,Age,Blood_Group,Address) values(%s,%s,%s,%s,%s,%s,%s);',
              (memberID, name, gender, dob, 0, blood, address))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * from Members_415')
    data = c.fetchall()
    return data


def view_events():
    c.execute('SELECT * from Event_415')
    data = c.fetchall()
    return data


def view_only_members():
    c.execute('SELECT Name FROM Members_415')
    data = c.fetchall()
    return data


def edit_details(new_memberID, new_name, new_gender, new_dob, Age, new_blood, new_address, memberID, name, gender, dob, blood, address):
    c.execute("UPDATE members_415 set member_id=%s,Name = %s,gender = %s,dob=%s,blood_group=%s,address=%s where member_id = %s and Name = %s and gender = %s and dob=%s and blood_group=%s and address=%s",
              (new_memberID, new_name, new_gender, new_dob, new_blood, new_address, memberID, name, gender, dob, blood, address))
    mydb.commit()
    data = c.fetchall()
    return data


def get_details(selected_member):
    c.execute(
        'SELECT * FROM members_415 WHERE name="{}"'.format(selected_member))
    data = c.fetchall()
    return data


def delete_data(selected_member):
    c.execute('DELETE from members_415 where name="{}"'.format(selected_member))
    mydb.commit()


def set_age():
    c.execute('Call getAge();')
    mydb.commit()

def set_count():
    c.execute('Call setVol();')
    mydb.commit()


def ret_query(command):
    try:
        c.execute(command)
        cols = [i[0] for i in c.description]
        data = c.fetchall()
        try:
            mydb.commit()
        except mysql.connector.Error as err:
            pass
        finally:
            return (0, data, cols)
    except mysql.connector.Error as err:
        return (1, err.msg, '')
