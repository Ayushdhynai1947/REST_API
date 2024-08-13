TABLE_NAME ='USER'
column_values = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

set_clause = ",".join([f"{column} = %s" for column in column_values.keys()])
values = list(column_values.values())
quesry= f"UPDATE {TABLE_NAME} SET {set_clause}" 
print(set_clause)
print(values)
print(quesry,values)