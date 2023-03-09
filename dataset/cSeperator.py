import argparse
import os
import re
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help='path\\to\input_file.ttl')
    args = parser.parse_args()

    if not os.path.isfile(args.fname):
        sys.exit(f'Unable to find {args.fname}')

    text = open(args.fname, 'r').read()

    results = re.findall(r'^<mb:mutant.+?> \.\n$', text, flags=re.DOTALL | re.MULTILINE)

    for ext in ['c', 'java']:
        fname_out = args.fname.replace('.ttl', f'.{ext}.ttl')
        ext_results = [result for result in results if f'.{ext}>' in result]
        with open(fname_out, 'w') as fout:
            fout.write('\n'.join(ext_results))


if __name__ == '__main__':
    main()