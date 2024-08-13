# TABLE_NAME ='USER'
# column_values = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
# filter_condition =None
# set_clause = ",".join([f"{column} = %s" for column in column_values.keys()])
# values = list(column_values.values())
# query= f"UPDATE {TABLE_NAME} SET {set_clause}" 
# query += f"{filter_condition}"
# print(set_clause)
# print(values)
# print(query,values)