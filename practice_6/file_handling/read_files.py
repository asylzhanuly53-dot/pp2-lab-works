file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")