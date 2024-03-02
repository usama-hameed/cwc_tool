import argparse
from pathlib import Path


def get_bytes(file):
    return file.stat().st_size


def get_line(file):
    with open(file, 'r', encoding="utf8") as f:
        return len(f.readlines())


def get_words(file):
    total_words = 0
    with open(file, 'r', encoding="utf8") as f:
        for words in f.readlines():
            total_words += len(words.split())

    return total_words


def get_characters(file):
    total_chars = 0
    with open(file, 'r', encoding="utf8") as f:
        for _ in f.read():
            total_chars += 1
    return total_chars


parser = argparse.ArgumentParser(description='wc tool')

parser.add_argument("path")
parser.add_argument('-c', action='store_true', help='Number of Bytes in File')
parser.add_argument('-l', action='store_true', help='Number of Lines in File')
parser.add_argument('-w', action='store_true', help='Number of Words in File')
parser.add_argument('-m', action='store_true', help='Number of Characters in File')
parser.add_argument('--optional', help='An optional argument')


args = parser.parse_args()

if args.path is None:
    print("------")

text_file = Path(args.path)

if args.c:
    print(get_bytes(text_file), text_file)

elif args.l:
    print(get_line(text_file), text_file)

elif args.w:
    print(get_words(text_file), text_file)

elif args.m:
    print(get_characters(text_file), text_file)

else:
    print(get_line(text_file), get_words(text_file), get_bytes(text_file), text_file)

