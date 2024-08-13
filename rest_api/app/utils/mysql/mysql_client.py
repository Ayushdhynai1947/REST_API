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
                if columns is None:
                    query = f"SELECT * FROM {table_name}"
                else:
                    columns_str= ','.join(columns)
                    query = f" SELECT {columns_str} FROM {table_name}"
                if filter_condition:
                    query += f" WHERE {filter_condition}"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                results = [dict(row) for row in rows]
                select_status = dict(status="success", results=results)
            else:
                error_message = "Please make the connection first"
                raise ConnectionError(error_message)
        except Exception as e:
            error_message = f"Failed to execute select: {e}"
            print(error_message)
            raise ConnectionError(error_message)
        return select_status
            
    
    
    def update(self, table_name, column_value, filter_condition=None):
        update_status = None
        try:
            set_clause = ", ".join([f"{column} = %s" for column in column_value.keys()])
            values = list(column_value.values())
            query = f"UPDATE {table_name} SET {set_clause}"
            
            if filter_condition:
                query += f" WHERE {filter_condition}"
                
            self.cursor.execute(query, values)
            self.db.commit()
            affected_rows = self.cursor.rowcount
            update_status = dict(status="success", affected_rows=affected_rows)
            
        except Exception as e:
            error_message = f"Error: {e} while updating {table_name} for {column_value} with filter condition {filter_condition}"
            raise Exception(error_message)
        
        return update_status

    
    
    
    def delete(self,table , filter_condition = None):
        delete_status = None
        
        try:
            
            query = f"DELETE FROM {table}"
            if filter_condition:
                query += f"{filter_condition}"
            
            self.cursor.execute(query)
            self.db.commit()
            affected_row = self.cursor.rowcount
            delete_status = dict(status = "sucess",affected_row = affected_row)
            return delete_status
        
        except Exception as e:
            error_message  = f"Error:{e} while deleting {table} with filter_condition {filter_condition}"
            raise Exception(error_message)
        
        return delete_status    
    
    
    def insert(self, table_name, column_value):
        insert_status = None
        try:
            # Construct the column names and placeholders for the SQL query
            columns = ", ".join(column_value.keys())
            placeholders = ", ".join(["%s"] * len(column_value))  # Use "%s" for each column value
            
            # Construct the SQL query
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            # Data to be inserted
            data = tuple(column_value.values())
            
            # Execute the query
            self.cursor.execute(query, data)
            self.db.commit()
            
            # Get the last inserted ID and the number of affected rows
            last_row_id = self.cursor.lastrowid
            insert_status = dict(status="success", affected_rows=self.cursor.rowcount, last_row_id=last_row_id)
        except Exception as e:
            # Handle and log the error
            error_message = f"Error: {e} while inserting into {table_name}, columns_values: {column_value}"
            print(error_message)
            insert_status = {"status": "error", "message": str(e)}
        
        return insert_status

    
    
            
        
        
        
        
        
        
        
        
        
        
        
    
    