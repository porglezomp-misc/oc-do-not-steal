import json
import sys

import oc_do_not_steal


def format_style(style):
    num_fmt = style.count('{')
    repeat_words = ['#words#'] * num_fmt
    return style.format(*repeat_words)


def main(paths):
    words, styles = oc_do_not_steal.load_words(paths)
    styles = [format_style(style) for style in styles]
    print(json.dumps({'origin': styles, 'words': words}))


if __name__ == '__main__':
    main(sys.argv[1:])
