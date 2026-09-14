import csv


def clean_customer_csv(filename):

    valid_customers = []
    invalid_count = 0

    with open("customer.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for customer in reader:

            name = customer["name"]
            age = customer["age"]
            email = customer["email"]

            # Check name
            if name == "":
                print(customer["id"], "Missing name")
                invalid_count += 1

            # Check age
            elif age == "":
                print(customer["id"], "Missing age")
                invalid_count += 1

            else:
                try:
                    age = int(age)

                    if age <= 0:
                        print(customer["id"], "Invalid age")
                        invalid_count += 1
                    elif email == "":
                        print(customer["id"], "Missing email")
                        invalid_count += 1
                    else:
                        customer["age"] = age
                        valid_customers.append(customer)

                except ValueError:
                    print(customer["id"], "Invalid age format")
                    invalid_count += 1

    print("Valid customers:", len(valid_customers))
    print("Invalid customers:", invalid_count)

    return valid_customers


customers = clean_customer_csv("customers_raw.csv")

print(customers)
            










            

                

 