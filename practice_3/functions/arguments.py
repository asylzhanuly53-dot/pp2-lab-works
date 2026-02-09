# A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing:
#  information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

# Example
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Default Parameter Values
# You can assign default values to parameters.
# If the function is called without an argument, it uses the default value:

# Example
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")



# Keyword Arguments
# You can send arguments with the key = value syntax.

# Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# This way, with keyword arguments, the order of the arguments does not matter.

# Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# Positional Arguments
# When you call a function with arguments without using keywords, 
# they are called positional arguments.

# Positional arguments must be in the correct order:

# Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# The order matters with positional arguments:

# Example
# Switching the order changes the result:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")