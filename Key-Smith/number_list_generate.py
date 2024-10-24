import os
import platform
import sys
import time

def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def generate_numbers_to_file():
    """Generates numbers from start to end and writes them to a file."""
    try:
        start = int(input("Enter the starting number (e.g., 0): "))
        end = int(input("Enter the ending number (e.g., 9999): "))
        
        if start > end:
            print("Error: The starting number should be less than or equal to the ending number.")
            return
        
        with open("generated_numbers_list.txt", "w") as file:
            for i in range(start, end + 1):
                file.write(f"{i}\n")
        
        print("Success: Numbers have been successfully written to 'generated_numbers_list.txt'.")
    except ValueError:
        print("Error: Please enter valid integers for both starting and ending numbers.")

if __name__ == "__main__":
    try:
        generate_numbers_to_file()
    except KeyboardInterrupt:
        print("\nExiting...")
        time.sleep(3)  
        exit()
