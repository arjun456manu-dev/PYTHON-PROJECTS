def clean_employees(employees):

    valid_employee = []
    invalid_count = 0
    total_salary = 0

    for d in employees:

        name = d["name"]
        salary = d["salary"]
        id = d["id"]

        if name == "":
            print(id, "missing name")
            invalid_count += 1
            continue

        try:
            salary = int(salary)

        except ValueError:
            print(id, "invalid salary format")
            invalid_count += 1
            continue

        valid_employee.append(d)
        total_salary += salary

    print("Valid employees:", len(valid_employee))
    print("Invalid employees:", invalid_count)
    print("Total salary:", total_salary)

    return valid_employee


print(clean_employees(employees))

            


               
               

                    