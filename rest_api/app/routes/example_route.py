from flask import Blueprint ,jsonify
from app.resources.employe_client import EmpResource



example_route = Blueprint('example_route',__name__)


emp_resource = EmpResource




example_route.add_url_rule('/employees', view_func=emp_resource.as_view('employees'),methods=['GET','POST'])
example_route.add_url_rule('/employees/<int:employee_id>', view_func=emp_resource.as_view('employee_detail'), methods=['GET', 'PUT', 'DELETE'])
# example_route.add_url_rule('/employees', view_func=emp_resource.post, methods=['POST'])



# ADD resourse(s) to the blueprint

# employee_details = Employee()




# example_route.add_url_rule('/employees',view_func=employee_details.as_view('employees'),methods=['GET'])


# def get_employees():
#     employees = employee_details.query.all()
#     # Here you can convert the employees to JSON or any other response format
#     return "List of employees"

