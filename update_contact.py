#insert record into contact table
#we have to import connection file to run sql statement
import connection as c 

#create cursor 
mycursor = c.database.cursor()

#input from user 
name = input("Enter contact name")
mobile = input("Enter mobile no")
email = input("Enter email address ")
id = int(input("Enter contact id "))

#create sql variable 
sql = "update contact set name=%s, mobile=%s, email=%s where id=%s"

values = [name,mobile,email,id]

#execute sql 
mycursor.execute(sql,values)

#save changes 
c.database.commit()

print(f"{mycursor.rowcount} rows updated successfully")