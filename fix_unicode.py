import os
import glob

# Map emojis to safe ASCII
emoji_map = {
    '[OK]': '[OK]',
    '[WARN]': '[WARN]',
    '[SUCCESS]': '[SUCCESS]',
    '[LAUNCH]': '[LAUNCH]',
    '[NOTE]': '[NOTE]',
    '[IDEA]': '[IDEA]',
    '[FIX]': '[FIX]',
    '[ERROR]': '[ERROR]',
    '[FATAL]': '[FATAL]',
    '[BOT]': '[BOT]',
    '[TARGET]': '[TARGET]',
    '[FIRE]': '[FIRE]',
    '[MAGIC]': '[MAGIC]',
    '[PROTECTED]': '[PROTECTED]',
    '->': '->',
    '*': '*'
}

for py_file in glob.glob('**/*.py', recursive=True):
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for emoji, replacement in emoji_map.items():
            content = content.replace(emoji, replacement)
        
        if content != original:
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {py_file}")
    except Exception as e:
        print(f"Error in {py_file}: {e}")

print("Unicode fix complete!")