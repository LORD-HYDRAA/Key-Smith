import os
import sys
import platform
import subprocess
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered_banner():
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
    creator = "Created by Lord Hydra (Mohammed Zaid Khan)"
    
    terminal_width = shutil.get_terminal_size().columns
    banner_lines = banner.split('\n')
    centered_banner = '\n'.join(line.center(terminal_width) for line in banner_lines)
    centered_creator = creator.center(terminal_width)
    
    print(f"{green}{centered_banner}{reset}")
    print(f"{green}{centered_creator}{reset}\n")

def run_script(script_name):
    clear_screen()
    print_centered_banner()
    try:
        if platform.system() == "Windows":
            subprocess.run(["python", f"{script_name}.py"], check=True)
        else:
            subprocess.run(["python3", f"{script_name}.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
    except FileNotFoundError:
        print(f"Error: {script_name}.py not found")
    input("\nPress Enter to return to main menu...")

def main_menu():
    while True:
        clear_screen()
        print_centered_banner()
        print("""
Main Menu:
1. Generate Word List
2. Generate Number List
3. Filter Word List/Number List
0. Exit
""")
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            run_script("word_list_generate")
        elif choice == "2":
            run_script("number_list_generate")
        elif choice == "3":
            run_script("word_list_filter")
        elif choice == "0":
            sys.exit(0)
        else:
            print("Invalid choice")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
