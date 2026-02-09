# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

# ExampleGet your own Python Server
def my_function():
  print("Hello from a function")

#   To call a function, write its name followed by parentheses:

# Example
def my_function():
  print("Hello from a function")

my_function()

# Why Use Functions?

# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program.
#  Without functions, you would have to write the same calculation code repeatedly:

# Example
# Without functions - repetitive code:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))