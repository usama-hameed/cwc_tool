import argparse
from pathlib import Path


def get_bytes(file):
    return file.stat().st_size


OPTIONS = {'c': get_bytes}


parser = argparse.ArgumentParser(description='wc tool')

parser.add_argument("path")
parser.add_argument('-c', action='store_true', help='Number of Bytes in File')

args = parser.parse_args()

text_file = Path(args.path)

if args.c:
    print(get_bytes(text_file), text_file)
