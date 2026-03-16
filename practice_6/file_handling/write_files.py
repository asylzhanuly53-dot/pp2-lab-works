file_name = "sample.txt"

# 1. Create and write
with open(file_name, "w") as file:
    file.write("First line of sample data.\n")
    file.write("Second line of sample data.\n")

# 3. Append and verify
with open(file_name, "a") as file:
    file.write("This is an appended line.\n")

print(f"File '{file_name}' created and updated.")