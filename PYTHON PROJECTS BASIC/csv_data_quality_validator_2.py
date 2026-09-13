customers = [
    {"id": 101, "name": "Rahul", "age": 22, "email": "rahul@gmail.com"},
    {"id": 102, "name": "Priya", "age": 25, "email": "priya@gmail.com"},
    {"id": 103, "name": "", "age": 31, "email": "aman@gmail.com"},
    {"id": 104, "name": "Neha", "age": -5, "email": "neha@gmail.com"},
    {"id": 105, "name": "Rohit", "age": 28, "email": ""},
    {"id": 106, "name": "Simran", "age": 19, "email": "simran@gmail.com"}
]

def valid_customers(customers):
    valid_list = []
  

    count = 0 

    for c in customers:
        if  c["name"] =="":
            print(c["id"] ,"missing name")
            count += 1

        elif c["age"] <= 0 :
            print(c["id"],"invalid age")
            count += 1

        elif c["email"] == "":
            print(c["id"] ,"missing email") 
            count += 1

        else:
            valid_list.append(c)
    print("invalid customers :" , count)        

    return(valid_list)
print(valid_customers(customers))        



