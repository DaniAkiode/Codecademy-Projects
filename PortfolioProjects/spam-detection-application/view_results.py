import sqlite3

def view_results():
    conn = sqlite3.connect("spam_results_with_model.db") #connect to database
    cursor = conn.cursor() # turn database into an object

    cursor.execute("SELECT * FROM results") # execute sql commands 
    rows = cursor.fetchall() # fetch all rows in the database 

    for row in rows:
        print(row) # print all stored messages and results
    
    conn.close() # close connection

view_results() # call function to view results 