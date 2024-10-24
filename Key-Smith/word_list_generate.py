import itertools
import os
import platform
import sys
from concurrent.futures import ThreadPoolExecutor
import time


def generate_leet_speak(word):
    substitutions = {
        'a': '@', 'i': '1', 'o': '0', 's': '$', 'e': '3', 't': '7', 'l': '1'
    }
    variations = set()
    variations.add(word)
    for old, new in substitutions.items():
        if old in word:
            variations.add(word.replace(old, new))
    return variations


def generate_combinations(word, numbers, special_chars, leet_speak):
    combinations = set()
    combinations.add(word)
    if leet_speak:
        leet_variations = generate_leet_speak(word)
        for leet_word in leet_variations:
            combinations.add(leet_word)
    for num in numbers:
        combinations.add(word + num)
        combinations.add(num + word)
        for char in special_chars:
            combinations.add(word + num + char)
            combinations.add(num + char + word)
            combinations.add(word + char)
            combinations.add(char + word)
    return combinations


def generate_wordlist(base_words, numbers, special_chars, leet_speak, max_workers=6):
    wordlist = set()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_combinations, word, numbers, special_chars, leet_speak) for word in base_words]
        for future in futures:
            wordlist.update(future.result())
    return wordlist


def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


try:
    first_name = input("Enter target's first name: ")
    last_name = input("Enter target's last name: ")

    base_words = [first_name, last_name, first_name + last_name, last_name + first_name]

    add_other_words = input("Do you want to add other words? (y/n): ")
    while add_other_words.lower() == 'y':
        other_word = input("Enter another word: ")
        base_words.extend([other_word, first_name + other_word, last_name + other_word])
        add_other_words = input("Do you want to add another word? (y/n): ")

    add_special_chars = input("Do you want to include special characters? (y/n): ")
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'] if add_special_chars.lower() == 'y' else []

    add_leet_speak = input("Do you want to include leet speak substitutions? (y/n): ")
    leet_speak = add_leet_speak.lower() == 'y'

    add_number = input("Do you want to add numbers to the passwords? (y/n): ")
    numbers = []
    if add_number.lower() == 'y':
        while True:
            try:
                start_range = int(input("Enter the starting number (e.g., 0): "))
                end_range = int(input("Enter the ending number (e.g., 9999): "))
                if start_range < end_range:
                    numbers = [str(i).zfill(len(str(end_range))) for i in range(start_range, end_range + 1)]
                    break
                else:
                    print("Starting number must be less than ending number.")
            except ValueError:
                print("Please enter valid numbers.")

    max_workers = int(input("Enter the number of threads (recommended: 2 or 4 for low-end PCs): "))

    wordlist = generate_wordlist(base_words, numbers, special_chars, leet_speak, max_workers)

    filtered_wordlist = [word for word in wordlist if 8 <= len(word) <= 20]

    with open('word_list.txt', 'w') as file:
        for word in filtered_wordlist:
            file.write(word + '\n')

    print(f"Word list generated and saved to word_list.txt. {len(filtered_wordlist)} words created.")

except KeyboardInterrupt:
    print("\nExiting...")
    time.sleep(3)
    sys.exit()
