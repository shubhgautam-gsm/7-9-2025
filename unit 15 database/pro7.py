import mysql.connector
#STEP 3 ADD DATA IN TABLE FEILDS
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="alratv_app")

    myCursor = connection.cursor()
    query = "INSERT INTO fruits (name, color, price) VALUES (%s, %s, %s)"
    data = [("apple", "red", "70rs"), ("grape", "green", "100rs")]
    
    myCursor.executemany(query, data)
    print("New Records Inserted")
    connection.commit()
    connection.close()
except Exception as err:
    if 'connection' in locals() and connection.is_connected():
        connection.rollback()
        connection.close()
    print("Error is ", err)
