from flask_restful import Resource
from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient


class MySQLResource(Resource):
    def get(self):
        config = ConfigClient(env='dev')
        mysql_uri= config.get_value("Database","uri3")
        mysql_client = MySQLClient(mysql_uri)
        
        
        try:
            # For selecting the data
            update_status = mysql_client.select(table_name="students" )
            
            
            # update_status = mysql_client.update(table_name="students", column_value={"age": 28},filter_condition= "name='Charlie Davis'")
            
            # update_status = mysql_client.insert(table_name="students", column_value={"name": "John Doe", "age": 21, "email": "john.doe@example.com", "course": "Computer Science", "enrollment_date": "2024-08-11"})
            
            return {'all details are ': update_status}
        except ConnectionError as e:
            return {'error': str(e)}
        except Exception as e:
            return {'error': f"An unexpected error occurred: {str(e)}"}
        
        
        
        
        # update_result = mysql_client.update("students", {"age": 22}, "name='John Doe'")
        # update_staus = mysql_client.update(table='students')
        
        
        # insert_result = mysql_client.insert("students", {"name": "John Doe", "age": 21, "email": "john.doe@example.com", "course": "Computer Science", "enrollment_date": "2024-08-11"})
       
    
        # Delete data
        # update_staus = mysql_client.delete("students", "name='John Doe'")
        
            
    
    
    
    def post(self):
        return {'message': 'Post request received'}