# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#   You can also have an else without the elif:

# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#   How Else Works
# The else statement provides a default action when none of the previous conditions are true. 
# Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

# Note: The else statement must come last. You cannot have an elif after an else.


# You can combine if, elif, and else to create a comprehensive decision-making structure.

# Example
# Temperature classifier:

# temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")