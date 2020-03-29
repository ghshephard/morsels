import argparse
import sys


def escape(c, style):
    if ord(c) <= 127:
        ch = c
    elif style == 'html':
        ch = f'&#x{ord(c):x};'
    elif ord(c) < 65535:
        ch = f'\\u{ord(c):04x}'
    else:
        ch = f'\\U{ord(c):08x}'
    return ch


def parse_file(fp, style):
    print(''.join(escape(c, style) for c in fp.read()), end="")


def main():
    parser = argparse.ArgumentParser(description='parse utf-8 files')
    parser.add_argument('file', type=argparse.FileType('rt'))
    parser.add_argument('--style', default='default', 
                        choices=['default', 'html'])
    args = parser.parse_args()
    parse_file(args.file, args.style)


if __name__ == "__main__":
    main()
