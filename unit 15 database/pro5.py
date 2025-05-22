import mysql.connector

#STEP 2 CREATE TABLE IN DATABASE alratv_app
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")

    myCursor = connection.cursor()
    query = "CREATE TABLE bca (Roll INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), City VARCHAR(255)\
    ,Contact INT(12))"
    result = myCursor.execute(query)
    print("Table Created")

    connection.close()
except Exception as err:
    print("Error is ", err)



