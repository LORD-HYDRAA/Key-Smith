import os
import sys
import shutil
from concurrent.futures import ThreadPoolExecutor

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

SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '~']
SEPARATORS = ['', '_', '.', '-', '@']
COMMON_NUMS = ['1', '12', '123', '1234', '12345', '111', '222', '000', '100', '200', '69', '6969', '1122', '99']
MAX_WORKERS = 6

def generate_leet_variations(word):
    leet_map = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7'],
        'b': ['8'],
        'g': ['9']
    }
    variations = {word}
    for char, subs in leet_map.items():
        if char in word.lower():
            new_vars = set()
            for variant in variations:
                for sub in subs:
                    new_vars.add(variant.replace(char, sub))
                    new_vars.add(variant.replace(char.upper(), sub))
            variations.update(new_vars)
    return variations

def generate_numbers(start, end):
    numbers = set(str(i) for i in range(start, end + 1))
    numbers.update(COMMON_NUMS)
    return sorted(numbers, key=lambda x: (len(x), x))

def generate_combinations(word, numbers, special_chars, leet_speak):
    combinations = set()
    combinations.add(word)
    
    if leet_speak:
        combinations.update(generate_leet_variations(word))
    
    for num in numbers:
        combinations.add(word + num)
        combinations.add(num + word)
        
        for char in special_chars:
            combinations.add(word + char)
            combinations.add(char + word)
            combinations.add(word + num + char)
            combinations.add(num + char + word)
            combinations.add(char + word + num)
            combinations.add(word + char + num)
    
    return combinations

def generate_wordlist(base_words, numbers, special_chars, leet_speak):
    wordlist = set()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for word in base_words:
            futures.append(executor.submit(
                generate_combinations, word, numbers, special_chars, leet_speak
            ))
        
        for future in futures:
            wordlist.update(future.result())
    
    return wordlist

def main():
    clear_screen()
    print_centered_banner()
    
    print("ULTIMATE Password Generator")
    print("--------------------------")
    
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    extra = input("Extra words (comma separated, optional): ").strip()
    
    base_words = {first, last, first + last, last + first,
                 first.lower(), last.lower(),
                 first.capitalize(), last.capitalize()}
    
    if extra:
        extra_words = [w.strip() for w in extra.split(',') if w.strip()]
        base_words.update(extra_words)
        for word in extra_words:
            base_words.add(first + word)
            base_words.add(word + first)
            base_words.add(last + word)
            base_words.add(word + last)
    
    use_special = input("Use special chars? (y/n): ").lower() == 'y'
    special_chars = SPECIAL_CHARS if use_special else ['']
    
    use_leet = input("Use leet speak? (y/n): ").lower() == 'y'
    
    use_numbers = input("Add numbers? (y/n): ").lower() == 'y'
    numbers = []
    if use_numbers:
        start = int(input("Start range (e.g., 0): "))
        end = int(input("End range (e.g., 9999): "))
        numbers = generate_numbers(start, end)
    
    print("\nGenerating passwords... (This may take a moment for large ranges)")
    wordlist = generate_wordlist(base_words, numbers, special_chars, use_leet)
    
    filtered = [p for p in wordlist if 6 <= len(p) <= 64]
    with open('wordlist.lst', 'w') as f:
        f.write('\n'.join(sorted(filtered, key=lambda x: (len(x), x))))
    
    print(f"\nGenerated {len(filtered)} passwords in wordlist.lst")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(0)
