# Step 1: File Read & Write Challenge 🖋️
try:
    with open("input.txt", "r") as file:
        content = file.read()

    modified_content = content.upper()  # Example modification

    with open("output.txt", "w") as file:
        file.write(modified_content)

    print("File has been modified and saved as 'output.txt'.")

except FileNotFoundError:
    print("Error: 'input.txt' not found. Please make sure the file exists.")

# Step 2: Error Handling Lab 🧪
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
