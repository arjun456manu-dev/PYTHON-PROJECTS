employee = input("Enter employee name: ")
print(f"employee name is {employee}")
monthly_salary = float(input("Enter monthly salary: "))
print(f"monthly salary is {monthly_salary}")
annual_salary = monthly_salary * 12
print(f"annual salary is {annual_salary}")
experience = int(input("enter your experience :"))
if experience >= 3:
    print(" you are eligible")
else:
    print("not eligible")


if monthly_salary > 60000:
    print("high")
    print("salary category = HIGH")
elif  30000 <= monthly_salary <= 60000 :
    print(" salary category : avegrage")
else:
    print("low")