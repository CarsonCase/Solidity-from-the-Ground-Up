import os
from dotenv import load_dotenv
import sys
if len(sys.argv) != 2:
    raise("ERROR: Must include the episode name")

# Load environment variables from .env
load_dotenv()

# Get the current number from the .env file
current_number = int(os.getenv("DAY"))
start_day = int(os.getenv("START_DAY"))

def createFile(folder, title, ext=".txt"):
    # Create a new file with the incremented number in the name
    new_file_name = f"{folder}/{current_number-start_day+1}_{title}{ext}"

    # Write something to the new file
    with open(new_file_name, "w") as new_file:
        new_file.write("This is a new file.")
    print(f"New file '{new_file_name}' created, and")

title = sys.argv[1]
createFile("postsRaw",title)
createFile("myNotes",title)
createFile("./", title,".md")

# Increment the number
new_number = current_number + 1
# Update the .env file with the new number
with open(".env", "w") as env_file:
    env_file.write(f"DAY={new_number}\n")
print("env updated with new day: {new_number}")