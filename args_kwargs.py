def calculate_total(price, quantity):
    total = price * quantity
    
    return total
print(calculate_total(23,56))


def create_profile(name, age, city):
    print(name)
    print(age)
    print(city)
create_profile("arjun" , 34 , 'lucknow')
create_profile(name="arjun" ,  age= 67 ,city= "lucknow")    


def greet (name , message= "welcomme"):
    print(name)
    print(message)
greet(name= "arjun")    
greet(name= "arjun" , message= "data science")    


def calculate_sum(*args):
    total = 0
    for arg in args:
        total += arg

    return total
print(calculate_sum(23,45,23))

def larges(*args):
    largest = args[0]
    for number in args:
        if number > largest:
            largest = number

    return largest
print(larges(23,45,65,3,2,5,4,3))        
