# Key Smith

Key Smith is a specialized tool for generating password and number lists, designed for ethical hacking and security assessments. Ideal for security professionals and researchers, Key Smith enables users to create diverse combinations of passwords and numeric sequences to test and strengthen the security of systems. Use it responsibly to identify vulnerabilities and enhance your cybersecurity posture.

## Key Smith Features

* **User Input for Personalization**:  
  Enter target's first and last names to tailor password generation.

* **Flexible Word Options**:  
  Choose to add additional words for enhanced complexity. The prompt will continue to ask for more words until the user indicates they are done by entering "n," allowing for a fully customized password generation experience.

* **Special Characters Inclusion**:  
  Option to integrate special characters for stronger password variations.

* **Leet Speak Support**:  
  Enable leet speak substitutions (e.g., replacing 'a' with '@') for creative passwords.

* **Numeric Combinations**:  
  Option to add a range of numbers to the generated passwords.

* **Customizable Number Range**:  
  Specify starting and ending numbers for numeric additions (e.g., 1 to 9999).

* **Multithreading Support**:  
  Set the number of threads for faster generation (recommended: 2 or 4 for low-end PCs; up to 6 for high-performance systems).

* **Output File**:  
  Generated word lists are saved in `word_list.txt`, providing easy access to all created combinations.

## Installation

To install Key Smith, follow these steps:

1. **Clone the repository:**  
   `git clone https://github.com/LORD-HYDRAA/Key-Smith.git` 

2. **Navigate to the project directory:**  
   `cd Key-Smith`
 
3. **Run the tool:**  
   `python3 Key-Smith.py`

## Disclaimer

Use **Key Smith** responsibly and only for ethical purposes. This tool is intended for security assessments, penetration testing, and educational use. Unauthorized use of this tool against systems or networks without explicit permission is illegal and unethical. Always ensure you have permission before testing the security of any system. 

**I am not responsible for any misuse or damage caused by this tool.**

## Recommendations

For users wanting to generate larger number ranges, we recommend splitting the range across multiple runs for better performance. For example:

- **First Run**: Use a range of **1 to 9999**.
- **Second Run**: Use a range of **10,000 to 999,999**.

This approach helps manage the output more efficiently and enhances the tool's performance.

## License

This project is licensed under the MIT License. Please give credit to the original creator when redistributing or modifying this tool. See the [MIT License](https://choosealicense.com/licenses/mit/) for details.
