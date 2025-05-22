import mysql.connector
#STEP 3 ADD DATA IN TABLE FEILDS
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")

    myCursor = connection.cursor()
    query = "INSERT INTO bca (Roll,Name,City,Contact) VALUES (%s, %s, %s,%s)"
    data = (1, "rajiv sheikh", "rajkot",7066947830)
    
    myCursor.execute(query, data)
    print("New Records Inserted")
    connection.commit()
    connection.close()
except Exception as err:
    if 'connection' in locals() and connection.is_connected():
        connection.rollback()
        connection.close()
    print("Error is ", err)
PERSON=''