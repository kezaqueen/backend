def add(a,b):
    answer=a+b
    return answer
def substract(a,b):
    answer=a-b
    return answer
def multiply(a,b):
    answer=a*b
    return answer
def divide(a,b):
    answer=a/b
    return answer
def modulus(a,b):
    answer=a%b
    return answer
def exponent(a,b):
    answer=a**b
    return answer
def square(a):
    answer=a**2
    return answer
def cube(a):
    answer=a**3
    return answer
def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
#the return should be outside the for loop but inside the function
