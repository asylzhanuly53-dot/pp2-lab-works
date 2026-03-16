import shutil
import os

os.makedirs("test_dir", exist_ok=True)
with open("temp.txt", "w") as f: f.write("temp")

# Move/copy
shutil.move("temp.txt", "test_dir/moved_temp.txt")
print("File moved to test_dir.")