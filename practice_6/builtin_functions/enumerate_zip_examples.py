names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# 3. enumerate() and zip()
print("Paired scores with indices:")
for index, (name, score) in enumerate(zip(names, scores)):
    print(f"{index}: {name} scored {score}")

# 4. Type checking and conversions
value = "100"
if isinstance(value, str):
    converted = int(value)
    print(f"Type of {value} was {type(value)}, now it is {type(converted)}")