from flask import Blueprint 

# from flask_restful import Api
from app.resources.employe_client import EmpResource
from app.resources.my_sqlresources import MySQLResource



#creating a blure print for route
example_route = Blueprint('example_route',__name__)



# Add  resource(s) to the blueprint
emp_resource = EmpResource



#Define a route within the Bluepint
example_route.add_url_rule('/mysql', view_func=mysql_resourcse.as_view('mysql'))


example_route.add_url_rule('/employees', view_func=emp_resource.as_view('employees'),methods=['GET','POST'])
example_route.add_url_rule('/employees/<int:employee_id>', view_func=emp_resource.as_view('employee_detail'), methods=['GET', 'PUT', 'DELETE'])
# example_route.add_url_rule('/employees', view_func=emp_resource.post, methods=['POST'])










# example_route.add_url_rule('/employees',view_func=employee_details.as_view('employees'),methods=['GET'])


# def get_employees():
#     employees = employee_details.query.all()
#     # Here you can convert the employees to JSON or any other response format
#     return "List of employees"

