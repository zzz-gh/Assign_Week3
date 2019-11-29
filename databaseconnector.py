import mysql.connector

def connect(): 
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root' ,
        passwd = '' ,
        
    )
    

    cursor = mydb.cursor()
    return mydb,cursor
 
