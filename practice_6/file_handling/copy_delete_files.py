import shutil
import os

source = "sample.txt"
destination = "sample_backup.txt"

# 4. Copy and backup
if os.path.exists(source):
    shutil.copy(source, destination)
    print(f"Backup created: {destination}")

# 5. Delete safely
file_to_delete = "sample_backup.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"File '{file_to_delete}' deleted safely.")