import mysql.connector

try:
    # Connect to MySQL database
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # Step 1: Add the new column 'id' to the table (added at the end by default)
    # add_column_query = "ALTER TABLE bca ADD COLUMN email VARCHAR(100)"
    # cursor.execute(add_column_query)

    # Step 2: Modify column order to position 'id' before 'fname'
    modify_column_order_query = "ALTER TABLE bca MODIFY COLUMN Contact INT(10) AFTER city"
    cursor.execute(modify_column_order_query)

    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

    print("Column 'id' added and positioned before 'fname' successfully")

except mysql.connector.Error as err:
    print("Error:", err)
