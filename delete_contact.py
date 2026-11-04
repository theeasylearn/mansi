#delete record into contact table
#we have to import connection file to run sql statement
import connection as c #c is alias (nick name)

#create cursor 
mycursor = c.database.cursor()

id = int(input("Enter contact id to delete "))
#create sql variable
sql = "delete from contact where id = %s" # %s (placeholder)
values = [id]

#run sql statement 
mycursor.execute(sql,values)

#save changes  
c.database.commit()
print(str(mycursor.rowcount) + " row has been deleted")
