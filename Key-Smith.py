import os
import shutil
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_custom_banner():
    green = "\033[92m"  
    reset = "\033[0m"   
    
    banner = """
  _  __             _____           _ _   _     
 | |/ /            / ____|         (_) | | |    
 | ' / ___ _   _  | (___  _ __ ___  _| |_| |__  
 |  < / _ \ | | |  \___ \| '_ ` _ \| | __| '_ \ 
 | . \  __/ |_| |  ____) | | | | | | | |_| | | |
 |_|\_\___|\__, | |_____/|_| |_| |_|_|\__|_| |_|
            __/ |                               
             |____/                                 

    """
    creator_line = "Created by Lord Hydra (Mohammed Zaid Khan)"
    
    terminal_width = shutil.get_terminal_size().columns
    banner_lines = banner.split('\n')
    centered_banner = '\n'.join(line.center(terminal_width) for line in banner_lines)
    centered_creator_line = creator_line.center(terminal_width)
    
    print(f"{green}{centered_banner}{reset}")
    print(f"{green}{centered_creator_line}{reset}")
    print() 

def print_main_menu():
    # Side menu options
    menu = """
Select a password generation mode:
  1. Word List
  2. Number List
  0. Exit
"""
    print(menu)

def get_input(prompt):
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)

def main():
    while True:
        clear_screen()
        print_custom_banner()
        print_main_menu()

        choice = get_input("Enter your choice: ")

        if choice == "0":
            print("\nExiting...")
            break
        elif choice == "1":
            clear_screen()  
            print_custom_banner() 
            try:
                subprocess.run(["python", "word_list_generate.py"], check=True) 
            except subprocess.CalledProcessError:
                print("\nAn error occurred while running the word list generator.")
            input("Press Enter to go back to the menu...")
        elif choice == "2":
            clear_screen()  
            print_custom_banner() 
            try:
                subprocess.run(["python", "number_list_generate.py"], check=True) 
            except subprocess.CalledProcessError:
                print("\nAn error occurred while running the number list generator.")
            input("Press Enter to go back to the menu...")
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
