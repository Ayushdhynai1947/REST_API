import mysql.connector
import json
from datetime import date





class MySQLClient():
    
    def __init__(self,mysql_uri) -> None:
        self.mysql_uri = mysql_uri
        db_conn = self.make_connection()
        self.db = db_conn
        
        if self.db:
            self.cursor = self.db.cursor(dictionary= True)
        else:
            self.cursor = None
            
    
    def make_connection(self):
        db = None
        try:
            db = mysql.connector.connect(host="localhost",user="root",password="ayush",database="students")
        
            print("connection succesfuly form")
        except Exception as e:
            error_message =f"Datbase connection fails{e}"
            print(error_message)
            raise ConnectionError(error_message)
        return db
    
    
    