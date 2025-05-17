import os
import re
import sys
from collections import defaultdict
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

class WordlistFilter:
    def __init__(self):
        self.wordlist = []
        self.filtered = []
        self.stats = defaultdict(int)
        self.common_weak = {
            'password', '123456', '12345678', '123456789', 'admin', 'qwerty',
            'letmein', 'welcome', 'monkey', 'password1', 'abc123', 'football'
        }
        self.date_patterns = [
            r'\d{4}', r'\d{6}', r'19\d{2}', r'20[0-2]\d',
            r'0[1-9]|1[0-2][0-3][0-9]', r'[0-3][0-9]0[1-9]|1[0-2]'
        ]

    def load_wordlist(self, filename='wordlist.lst'):
        if not os.path.exists(filename):
            print(f"Error: {filename} not found")
            return False
        
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            self.wordlist = [line.strip() for line in f if line.strip()]
        return True

    def save_results(self, filename='wordlist_filtered.lst'):
        with open(filename, 'w') as f:
            f.write('\n'.join(self.filtered))
        print(f"\nSaved {len(self.filtered)} passwords to {filename}")

    def show_stats(self):
        avg_len = sum(len(p) for p in self.filtered)/len(self.filtered) if self.filtered else 0
        print("\nStatistics:")
        print(f"- Total passwords: {len(self.filtered)}")
        print(f"- Average length: {avg_len:.1f}")
        print(f"- Contains numbers: {sum(any(c.isdigit() for c in p) for p in self.filtered)}")
        print(f"- Contains special: {sum(any(not c.isalnum() for c in p) for p in self.filtered)}")
        print(f"- Mixed case: {sum(any(c.islower() for c in p) and any(c.isupper() for c in p) for p in self.filtered)}")
        
        for opt, count in self.stats.items():
            if count > 0:
                print(f"- {opt}: {count}")

    def show_menu(self):
        print("""
Filter Options:
1. Remove duplicates
2. Remove blank/empty lines
3. Remove pure numbers
4. Remove pure alphabetic words
5. Remove pure special characters
6. Keep only with special characters
7. Keep only with numbers
8. Keep only with letters+numbers
9. Keep only mixed case
10. Remove single case passwords
11. Remove <8 characters
12. Remove >64 characters
13. Custom length range
14. Remove sequential patterns
15. Remove date patterns
16. Remove repetitive characters
17. Remove mirrored strings
18. Remove common weak passwords
19. REGEX filter
20. Character type requirements
21. Exclude dictionary words
22. Sort output
23. Show statistics
24. Limit total passwords
25. Save results
0. Back to main menu

Enter choices (comma separated): """)
        return input().strip()

    def run(self):
        clear_screen()
        print_centered_banner()
        if not self.load_wordlist():
            input("Press Enter to continue...")
            return
        
        while True:
            clear_screen()
            print_centered_banner()
            print(f"Current password count: {len(self.filtered)}")
            options = self.show_menu().split(',')
            
            if '0' in options:
                break
            
            if '23' in options:
                clear_screen()
                print_centered_banner()
                self.show_stats()
            elif '25' in options:
                filename = input("Output filename (default: filtered.lst): ") or 'filtered.lst'
                self.save_results(filename)
            else:
                self.apply_filters(options)
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    WordlistFilter().run()
