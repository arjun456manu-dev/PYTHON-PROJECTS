customers = [
    {"id": 101, "name": "Rahul", "age": 22, "email": "rahul@gmail.com"},
    {"id": 102, "name": "Priya", "age": 25, "email": "priya@gmail.com"},
    {"id": 103, "name": "", "age": 31, "email": "aman@gmail.com"},
    {"id": 104, "name": "Neha", "age": -5, "email": "neha@gmail.com"},
    {"id": 105, "name": "Rohit", "age": 28, "email": ""},
    {"id": 106, "name": "Simran", "age": 19, "email": "simran@gmail.com"}
]

def validate_customers(customers):
    valid_list = []
    for c in customers:
        if c["name"] == "" or c["age"] <= 0 or c["email"] == "":
            continue
        else:
            valid_list.append(c)

    count = 0
    for c in customers:
        if c["name"] == "" or c["age"] <= 0 or c["email"] =="":
            count += 1
    print(count) 


    return(valid_list)
print(validate_customers(customers))

