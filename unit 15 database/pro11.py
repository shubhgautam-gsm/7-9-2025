import mysql.connector

try:
    # create connection and cursor objects
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # build a query
    query = "select * from bca where city = 'rajkot'"

    # execute query
    cursor.execute(query)

    # get result from executed cursor
    result = cursor.fetchall()

    # run loop on result and print all the data
    for row in result:
        print(row)

    connection.commit()
    connection.close()
except Exception as err:
    connection.rollback()
    print("Error is ",err)
