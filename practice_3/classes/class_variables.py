# Class Variables
# A class variable is a variable that belongs to the class itself rather than to any specific object.
#  All instances of the class share the same copy of this variable.

# Defined inside the class but outside all methods
# Accessed using the class name or an object
# Memory is allocated only once



class Student:
    school = "ABC School"   # Class variable
​
s1 = Student()
s2 = Student()
​
print(s1.school)
print(s2.school)

# Output
# ABC School
# ABC School
# Explanation:

# school is a class variable
# Both s1 and s2 share the same value
# The variable belongs to the class, not to individual objects


# Instance Variables
# Instance variables are variables that belong to a specific object
# . Each object maintains its own copy of these variables.

# Defined inside methods (usually __init__())
# Unique for each object
# Changes affect only that particular object



class Student:
    def __init__(self, name):
        self.name = name   # Instance variable
​
s1 = Student("Jake")
s2 = Student("Emily")
​
print(s1.name)
print(s2.name)

# Output
# Jake
# Emily
# Explanation:

# name is an instance variable
# Each object has its own value
# Changing one object’s value does not affect the other


# Example: Class Variable vs Instance Variable
# This example demonstrates how class variables are shared and instance variables remain separate.




class CSStudent:
    stream = 'cse'          # Class variable
​
    def __init__(self, name, roll):
        self.name = name    # Instance variable
        self.roll = roll    # Instance variable
​
# Creating objects
a = CSStudent('Rose', 1)
b = CSStudent('Nat', 2)
​
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)

# Output
# cse
# cse
# Rose
# Nat
# Explanation:

# stream is shared by all objects
# name and roll are unique for each object
# Both objects access the same class variable