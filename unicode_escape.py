import argparse
import sys


def parse_file(fp, style):
    line: str = ''
    for c in fp.readline():
        if ord(c) <= 127:
            ch: str = c
        elif style == 'html':
            ch: str = f'&#x{ord(c):x}'
        elif ord(c) < 65535:              
            ch: str = f'\\u{ord(c):04x}'
        else:
            ch: str = f'\\U{ord(c):08x}'
        line += ch
    print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='parse utf-8 files')
    parser.add_argument('filename')
    parser.add_argument('--style', default='default', 
                        choices=['default', 'html'])
    args = parser.parse_args()
    fn = args.filename
    if fn == '-':
        fp = sys.stdin
    else:  
        fp = open(fn, 'r', encoding='utf-8')

    parse_file(fp,args.style)
