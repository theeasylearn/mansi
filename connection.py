# import mysql connector
import mysql.connector as con 
try:
    #create database connection
    database = con.connect(host='localhost',user='root',passwd='',database='ds12',port=3306)
except con.Error as e:
    #this block will execute only in case of run time error
    print("error in establishing connection")
    print(e.errno)
    print(e.msg)
else:
    # this block will execute only if there is no run time error
    print("connection created....")
# finally:
    # print("Program finished")