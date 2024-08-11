import sqlite3



# class Raw_SQLClient:
    
#     def __init__(self,raw_sql_uri) -> None:
#         self.raw_sql_uri= raw_sql_uri
#         db_conn = self.make_connection()
#         self.db = db_conn
        
#         if self.db:
#             self.cursor= self.db.cursor(dictionary =True)
#         else :
#             self.cursor = None
    
    
    
#     def make_connection(self):
#         db = None
#         try :
            
#             db = sqlite3.connect(self.raw_sql_uri)
            
#             print("Connection Seccesfully form")
#         except Exception as e:
#             error_message = f"Datbase connection fails{e}"
#             print(error_message)
#             raise ConnectionError(error_message)
        
#         return db
    
#     def select(self,id):
        
            
            
            








