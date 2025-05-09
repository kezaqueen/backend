def hello():
    print("Hello AkiraChix")
def say_hello(name):
    print(f"hello {name}")
def greet(name,age):
    year=2025-age
    print(f"Hello{name}, born in {year}")
def greetings(names):
    for name in names:
        print(f"Hello {name}")
def year_0f_birth(name,age):
    year=2025-age
    print(f"Hello {name},born in {year}")
def my_country(name="Rwanda"):
    print(f"I love my country {name}")
def welcome_students(**kwargs):
    print(kwargs)
def create_sentence(**words):
    sentence=" "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence         
def unique(x):
    my_set = set(x)
    my_list= list(my_set)
    print(my_list)
unique(["okay","ok","okay","okey"])   











