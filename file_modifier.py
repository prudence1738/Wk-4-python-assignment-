# File Read & Write with User-Selected Modification and Error Handling

# Ask the user for the original filename
original_filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(original_filename, "r") as infile:
        content = infile.read()
    
    # Let the user choose a modification
    print("\nChoose a modification for the content:")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Add a custom string to each line")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        modified_content = content.upper()
    elif choice == "2":
        modified_content = content.lower()
    elif choice == "3":
        custom_string = input("Enter the string to add to each line: ")
        # Add custom string to each line
        lines = content.splitlines()
        modified_content = "\n".join([line + custom_string for line in lines])
    else:
        print("Invalid choice. The original content will be saved.")
        modified_content = content
    
    # Ask the user for the new filename
    new_filename = input("Enter the filename to save the modified content: ")
    
    # Write the modified content to the new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f"\nSuccess! Modified file created: {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{original_filename}' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read/write the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
