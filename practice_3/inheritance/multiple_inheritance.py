# Add Properties
# Example
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
# In the example below, the year 2019 should be a variable,
# and passed into the Student class when creating student objects.
# To do so, add another parameter in the __init__() function:

# Example
# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
