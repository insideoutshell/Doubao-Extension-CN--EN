import re
import json
import ast

# Read the JavaScript file content
with open("static/js/i18n_resources.js", 'r', encoding='utf-8') as f:
    content = f.read()

# Find all JSON.parse instances
json_pattern = r"JSON\.parse\('(?:[^'\\]|\\.)*?'\)"
matches = re.findall(json_pattern, content)

# Process translation entries
translations = {}
with open("combined_chunks.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            try:
                translations[key] = ast.literal_eval(value.strip())
            except (SyntaxError, ValueError):
                print(f"Failed to evaluate value for key '{key}': {value.strip()}")
                translations[key] = value.strip()  # Fallback to raw value
        else:
            print(f"Malformed entry skipped: {line}")

# Replace JSON.parse instances with actual translations
updated_content = content
for match in matches:
    updated_content = updated_content.replace(match, json.dumps(translations))

# Write updated content back to the JavaScript file
with open("static/js/i18n_resources.js", 'w', encoding='utf-8') as f:
    f.write(updated_content)
