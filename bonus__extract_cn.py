"""Tossing this in but it's not necessary unless you were curious. This is how the Chinese dictionary was extracted from the js.
Also, I split the output into 300 line chunks and translated with Gemini.

mkdir -p chunks && split -l 300 -d --additional-suffix=.txt i18n_list.txt chunks/chunk_ 
cat chunks/* > combined_chunks.txt

Roo Code prompt:
"Alright Gemini, I have an important mission for you. Your task is very simple. You must translate all the chunk files inside the chunks folder, but having the line scheme of Keep_identifier=Translated where Keep_identifier is the part before the equal sign that must be preserved, followed by the translated version of the Chinese that follows.  Also, make sure to retain any escapes or parse strings in their original format. Please do your best at translating these files, you're the only one capable of executing this mission. Go through each file, translate all the lines, then apply the differences by using either write file command or apply_diff, do not show it in chat. The context of these translations is for the Doubao chrome extension. Do not create any scripts and you don't need any external services, you're the one translating. Don't do line by line, try to translate the whole file at once. Good luck soldier! I'm turning on auto approve now.

EDIT (IMPORTANT: We've already translated chunk_00-chunk_09, continue at chunk_10"""
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
