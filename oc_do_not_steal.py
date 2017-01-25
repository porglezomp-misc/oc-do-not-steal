import sys
import random
import os

words = []
styles = []

def visit(args, dirname, names):
    for name in names:
        path = os.path.join(dirname, name)
        try:
            if name[-6:] == '.words':
                words.extend(open(path).read().split('\n'))
            if name[-7:] == '.styles':
                styles.extend(open(path).read().split('\n'))
        except IOError:
            pass

files = sys.argv[1:]
for base in files:
    os.path.walk(base, visit, None)

words = list({word.strip() for word in words if word.strip()})
styles = list({style.strip() for style in styles if style.strip()})

if not words:
    print("No words found!")
    exit(1)

print(random.choice(styles).format(
    *(random.choice(words).capitalize() for _ in range(10))
))
