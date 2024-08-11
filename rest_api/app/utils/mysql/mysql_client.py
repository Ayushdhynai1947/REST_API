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
    
    def select(self,table_name , columns =None ,filter_condition =None):
        results = []
        select_status = None
        try:
            if self.db is not None:
                if columns in None:
                    query = f"SELECT * FROM {table_name}"
                else:
                    columns_str= ',',join(columns)
                    query = f"SELECT{columns_str} FROM {table_name}"
                if filter_condition:
                    query += f"WHERE {filter_condition}"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                results = [dict(row) for row in rows]
                select_status = dict(status="success", results=results)
        else:
            error_message = ""
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    