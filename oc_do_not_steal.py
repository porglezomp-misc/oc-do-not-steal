import os
import random
import sys


def load_words(paths):
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

    for base in paths:
        os.path.walk(base, visit, None)

    words = list({word.strip() for word in words if word.strip()})
    styles = list({style.strip() for style in styles if style.strip()})
    return words, styles


def main(paths):
    words, styles = load_words(paths)
    if not words:
        print("No words found!")
        raise Exception("No words found!")

    print(random.choice(styles).format(
        *(random.choice(words).capitalize() for _ in range(10))
    ))


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except:
        sys.exit(1)
