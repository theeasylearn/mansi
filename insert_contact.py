#insert record into contact table
#we have to import connection file to run sql statement
import connection as c

#create cursor 
mycursor = c.database.cursor()

name = input("Enter contact name")
mobile = input("Enter mobile no")
email = input("Enter email address ")
#create sql variable 
# sql = "insert into contact (name,mobile,email) values ('ram','1234567890','theeasylearn@gmail.com')"
sql = "insert into contact (name,mobile,email) values (%s,%s,%s)" # %s = placeholder
values = [name,mobile,email]

#run sql statement 
mycursor.execute(sql,values)

#we must commit to save changes into database
c.database.commit()

print(mycursor.rowcount , " row inserted")