employee = {
    "name": "Arjun",
    "department": "Data",
    "salary": 55000,
    "performance": 82,
    "experience": 2
}

def employee_report(employee):
    print(employee["name"])
    print(employee["department"])
    annual_salary = (employee["salary"]* 12)
    print(annual_salary)
    if  80 <= employee["performance"]  <= 100:
        print("performance category : excellent")
    elif 60 <= employee["performance"] <= 70:
        print("good")
    elif 40 <= employee["performance"] <=59:
        print("average")
    elif employee["performace"] < 40:
        print("poor")
    else:
        print("very poor")
    if employee["performance"] >= 80 and employee["experience"] >= 2:
        print("eligible for bonus performance")
employee_report(employee)





