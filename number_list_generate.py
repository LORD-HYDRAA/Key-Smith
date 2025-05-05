import os
import shutil
import sys

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

def main():
    clear_screen()
    print_centered_banner()
    
    print("Number List Generator")
    print("--------------------")
    
    try:
        start = int(input("Start number: "))
        end = int(input("End number: "))
        step = int(input("Step (default 1): ") or 1)
        
        if start > end:
            print("Error: Start must be less than end")
            return
        
        with open('numbers.lst', 'w') as f:
            f.write('\n'.join(str(i) for i in range(start, end+1, step)))
        print(f"\nGenerated numbers from {start} to {end} (step {step}) in numbers.lst")
        
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
    except Exception as e:
        print(f"\nError: {str(e)}")
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
