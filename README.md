# 🔐 Key Smith

**Key Smith** is a specialized tool for generating password and number lists, designed for **ethical hacking** and **security assessments**. Ideal for security professionals and researchers, Key Smith enables users to create diverse combinations of passwords and numeric sequences to test and strengthen the security of systems.

> ⚠️ Use it responsibly to identify vulnerabilities and enhance your cybersecurity posture.

---

## 🛠️ Key Smith Features

### 🔹 User Input for Personalization
- Enter target's **first and last names** to tailor password generation.

### 🔹 Flexible Word Options
- Add additional words for enhanced complexity.
- The tool allows you to input as many words as you want.
- Type **`n`** when you're done to stop adding more words.

### 🔹 Special Characters Inclusion
- Option to integrate special characters (e.g., `!`, `@`, `#`, etc.) for stronger password variations.

### 🔹 Leet Speak Support
- Enable **leet speak** substitutions:
  - `a → @`, `i → 1`, `e → 3`, `o → 0`, `s → $`, `t → 7`, `l → 1`, etc.

### 🔹 Numeric Combinations
- Add a custom **range of numbers** to generate realistic variations (e.g., `john123`, `123john!`).

### 🔹 Customizable Number Range
- Specify the **starting** and **ending** numbers (e.g., `1` to `9999`).

### 🔹 Multithreading Support
- Increase speed using **multithreading**:
  - Recommended: `2–4` threads for low-end PCs
  - Up to `6` threads for high-performance machines

### 🔹 Output File
- Word lists are saved as:  
  - `word_list.lst` (for passwords)  
  - `number_list.lst` (for numeric sequences)

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LORD-HYDRAA/Key-Smith.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Key-Smith
   ```

3. **Run the tool:**
   ```bash
   python3 Key-Smith.py
   ```

---

## ⚠️ Disclaimer

Key Smith is intended **only** for:
- **Ethical hacking**
- **Security assessments**
- **Educational use**

> ❗ Do **not** use this tool against systems or networks without **explicit permission**. Unauthorized usage is **illegal** and **unethical**.

I, the creator, am **not responsible** for any misuse, damage, or consequences caused by this tool.

---

## 💡 Recommendations

For generating **large number ranges**, split them across multiple runs for better performance:

- **First Run:** 1 to 9,999  
- **Second Run:** 10,000 to 999,999  
- **Third Run:** 1,000,000 to 999,999,999  

This method helps optimize speed and manage file size efficiently.

---

## 📄 License

This project is licensed under the **MIT License**.

> Please give credit to the original creator  
> **// Created by Lord Hydra (Mohammed Zaid Khan)**  
> when redistributing or modifying this tool.

[MIT License](https://opensource.org/licenses/MIT)

---
