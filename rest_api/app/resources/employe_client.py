from flask_restful import Resource
from flask import  request ,jsonify
from app.model.models import Employee
from app import db
from datetime import datetime



class EmpResource(Resource):

    def get(self, employee_id=None):
        try:
            if employee_id:
                # Retrieve a specific employee by ID
                employee = Employee.query.get(employee_id)
                if employee:
                    return jsonify({
                        'id': employee.id,
                        'name': employee.name,
                        'email': employee.email,
                        'date_of_birth': str(employee.date_of_birth),
                        'phone_number': employee.phone_number
                    })
                return {'message': 'Employee not found'}, 404

            # Retrieve all employees if no ID is provided
            employees = Employee.query.all()
            employee_list = [{
                'id': e.id,
                'name': e.name,
                'email': e.email,
                'date_of_birth': str(e.date_of_birth),
                'phone_number': e.phone_number
            } for e in employees]
            return jsonify(employee_list)
        except Exception as e:
            return {'error': f'An unexpected error occurred: {str(e)}'}, 500

    def post(self):
        try :
            data = request.json
            
            date_of_birth_str = data.get('date_of_birth')
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
            
            new_employee = Employee(
                name = data.get('name'),
                email = data.get('email'),
                date_of_birth = date_of_birth,
                phone_number = data.get('phone_number')
            )
            db.session.add(new_employee)
            db.session.commit()
            return jsonify({'message':'Employee created successfully','employee':{
                'id': new_employee.id,
                'name':new_employee.name,
                'email': new_employee.email,
                'date_of_birth':str(new_employee.date_of_birth),
                'phone_number': new_employee.phone_number
            }}), 201
        except Exception as e:
            return {'error': f'An error occured while creating the employee:{str(e)}'},500
        
    def put(self,employee_id):
        try:
            data = request.json
            employee = Employee.query.get(employee_id)
            if not employee:
                return { 'message': 'Employee not found'}, 404
            
