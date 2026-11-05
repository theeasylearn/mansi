import connection as c 

#create cursor 
'''
() parenthesis -> tuple
[] bracket -> list 
{} braces -> dictionary 
'''
mycursor = c.database.cursor(dictionary=True)
# mycursor = c.database.cursor()

#create sql variable
sql = "select id,name,mobile,email from contact"

#execute sql statement 
mycursor.execute(sql)

single_row = mycursor.fetchone()
# print(single_row)
#fetch all rows
table = mycursor.fetchall()
line = f"{'id':<10} {'name':<32} {'mobile':15} {'email'}"
print(line)
print("-"*110)
count = 1
for row in table:
    line = f"{count} {row['id']:<10} {row['name']:<32} {row['mobile']:15} {row['email']}"
    print(line)
    count=count+1
    if count%15==0:
        key = input("Press any key to continue")
