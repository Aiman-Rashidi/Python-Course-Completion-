user_data1 = {
    "name": "Aiman",
    "age": 20,
    "location": "Delhi"
}

user_data2 = {
    "email": "aiman@example.com",
    "location": "Mumbai"
}

merged_data_1 = user_data1 | user_data2
print(merged_data_1)

merged_data_2 = {**user_data1, **user_data2}
print(merged_data_2)