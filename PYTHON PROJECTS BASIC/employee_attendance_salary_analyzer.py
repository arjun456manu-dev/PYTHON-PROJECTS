employees = {
    "Rahul": {"salary": 45000, "days_present": 24, "performance": 82},
    "Priya": {"salary": 52000, "days_present": 27, "performance": 91},
    "Aman": {"salary": 38000, "days_present": 19, "performance": 67},
    "Neha": {"salary": 60000, "days_present": 26, "performance": 88},
    "Rohit": {"salary": 42000, "days_present": 21, "performance": 74}
}

def employee_report(employees):
    total_salary = 0
    for name , details in employees.items():
        total_salary += details["salary"]
    print(total_salary)

    average_salary = total_salary / len(details)
    print(average_salary)

    highest_salary = max(employees ,key=lambda x: employees[x]["salary"])
    print(highest_salary)
    print(employees[highest_salary])

    count = 0
    for  details in employees.values():
        if details["days_present"] < 22:
            count += 1
    print(count) 

    for name , details in employees.items():
        if details["performance"] > 80:
            print(name ,"excellent")
        elif 60 < details["performance"] < 70:
            print( name ,"good")
        else:
           print( name ,"need improvement")

    for name , details in employees.items():
        if details["performance"] >= 85 and details["days_present"] >= 25:
            print(name,"bonus granted")
        else:
            print(name ,"no bonus")

employee_report(employees)
