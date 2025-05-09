def check_if_even(number):
    if number%2==0:
        print(f"{number} is even")
def check_if_even_or_odd(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")            
def check_divisibility(n):
    for x in range(1,n+1):
        if x%2==0:
            print(f"{x} is divisible by 2")
        elif x%3==0:
            print(f"{x} is divisible by 3")
        elif x%5==0:
            print(f"{x} is divisible 5")
        elif x%7==0:
            print(f"{x} is divisible by 7")    
        else:
            print(f"{x} is not divisible by 2,3, or 5") 
def fizz_buzz(n):
    for i in range(1,n):
        if i%2==0:
            print(f"{i} is fizz")
        elif i%3==0:
            print(f"{i} is buzz")
        elif i%5==0:
            print(f"{i} is fizzbuzz") 
        else:
            print("none") 
def countdown(start):
    while start >=0:
        print(f"countdown at {start}")
        start-=1                                            
def countdown_with_break(start,stop):
    while start >=0 :
        print(f"countdown at {start}")
        if start==stop:
            print(f"stopping at {stop}")
            break
        start-=1  
def countdown_with_odd_numbers(start):
    while start >=0:
        if start%2==0:
            start-=1
            continue
        print(F"countdown at {start}")
        start-=1 
#using  a while loop create a function to print all the even numbers between 0 and 100 
def first_hundred_even_numbers():
    n=0
    while n<=100:
        if n%2!=0:
            n+=1
            continue
        print(n)
        n+=1 
            

