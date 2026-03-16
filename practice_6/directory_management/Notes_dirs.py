import os

# 1. Create nested directories
path = "parent/child/grandchild"
os.makedirs(path, exist_ok=True)

# 2. List files and folders
print("Current directory structure:")
for root, dirs, files in os.walk("."):
    print(f"Root: {root}, Dirs: {dirs}, Files: {files}")

# 3. Find files by extension
print("\nPython files in current directory:")
files = [f for f in os.listdir('.') if f.endswith('.py')]
print(files)