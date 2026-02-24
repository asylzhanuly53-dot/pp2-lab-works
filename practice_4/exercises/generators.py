#1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

for square in square_generator(5):
    print(square)

 #2

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("Enter a number: "))
print(", ".join(even_generator(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter range limit: "))
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Start: "))
b = int(input("End: "))

for val in squares(a, b):
    print(val)

 #5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Start countdown from: "))
for number in countdown(n):
    print(number)       