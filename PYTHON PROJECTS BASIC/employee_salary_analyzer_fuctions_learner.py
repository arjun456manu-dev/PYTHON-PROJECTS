salaries = [32000, 45000, 28000, 60000, 52000, 39000]

def calculate_total(salaries):
    total_salaries = sum(salaries)
    return total_salaries

def calculate_avg(salaries):
    if len(salaries) == 0:
        return 0
    return sum(salaries)/len(salaries)

def find_highest(salaries):
    highest = max(salaries)
    return highest

def get_above_avg(salaries):
    above_avg = []

    for salary in salaries:
        average = calculate_avg(salaries)
        if salary > average:
            above_avg.append(salary)
    return above_avg

def generate_report(salaries):
    print("total salaries" ,calculate_total(salaries))
    print("average salaries" ,calculate_avg(salaries))
    print("highest salary" ,find_highest(salaries))
    print("above average salaries" ,get_above_avg(salaries))

generate_report(salaries)
    

        
