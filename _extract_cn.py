"""Tossing this in but it's not necessary unless you were curious. This is how the Chinese dictionary was extracted from the js. I split the output into 300 chunks and translated with Gemini."""
import os
import re
import json
import subprocess
import tempfile
content = open("static/js/i18n_resources.js", 'r', encoding='utf-8').read()
json_pattern = r"JSON\.parse\('((?:[^'\\]|\\.)*?)'\)"
match = re.search(json_pattern, content).group(1)
js_content = f"console.log('{match}')"

with tempfile.NamedTemporaryFile(suffix='.js', delete=False) as temp_file:
    temp_path = temp_file.name
    temp_file.write(js_content.encode('utf-8'))

process = subprocess.run(['node', temp_path], capture_output=True, text=True)
os.unlink(temp_path)
parsed_json = json.loads(process.stdout)
with open("i18n_list.txt", 'w', encoding='utf-8') as f:
    plain_format = '\n'.join([f"{k}={repr(v)}" for k, v in parsed_json.items()])
    f.write(plain_format)
