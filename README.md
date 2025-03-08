# Doubao-Extension-CN--EN

## Project Overview
This project focuses on translating the Doubao browser extension to English. The main goal is to make the extension more accessible to a wider range of users who are more comfortable using English.

## How It Works
The translation process involves several key steps:

### 1. Source Files
- `combined_chunks.txt`: This file contains all the translation entries in the format of `key=value`. These key-value pairs represent the original text and its corresponding English translation.
- `static/js/i18n_resources.js`: This JavaScript file contains the original language strings that need to be translated. It uses `JSON.parse` to handle the strings.

### 2. Translation Script
The `apply_translations.py` script is responsible for performing the actual translation. Here's a breakdown of what it does:
- **Reading the JavaScript File**: It reads the content of `static/js/i18n_resources.js` and finds all instances of `JSON.parse` using regular expressions.
- **Processing Translation Entries**: It reads the `combined_chunks.txt` file line by line, parses the key-value pairs, and stores them in a dictionary. If there are any issues with parsing the value, it will print an error message and use the raw value as a fallback.
- **Replacing Strings**: It replaces all the `JSON.parse` instances in the JavaScript file with the actual translated strings from the dictionary.
- **Writing the Updated File**: Finally, it writes the updated content back to the `static/js/i18n_resources.js` file.

## Usage
To use this translation project, follow these steps:

1. Make sure you have all the source files (`combined_chunks.txt` and `static/js/i18n_resources.js`) in the correct directory.
2. Run the `apply_translations.py` script using Python. You can do this by opening your terminal or command prompt, navigating to the project directory, and running the following command:
   ```sh
   python apply_translations.py
   ```
3. Check the `static/js/i18n_resources.js` file to see the updated content with the translated strings.
