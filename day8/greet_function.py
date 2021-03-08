def greet():
    print("Hello everyone! how is everybody doing?")
    print("welcome to the MPatra's shop")
    print("This is just an exploration \n")


greet()


# function that allows for input
def greet_with_name(name):
    print(f"Hello {name}! how is everybody doing?")
    print("welcome to the MPatra's shop")
    print("This is just an exploration\n")


greet_with_name('pilu')


# functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}\n")


greet_with('Pilu', 'Berhampur')

# function call with keyword arguments
greet_with(location='Odisha', name='Dipu')