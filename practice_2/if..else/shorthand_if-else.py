# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example
# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B")

# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

# Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# The syntax follows this pattern:

variable = value_if_true if condition else value_if_false

# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:

# Example
# One line, three outcomes:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")