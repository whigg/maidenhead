#!/usr/bin/env python
import maidenhead
from argparse import ArgumentParser
import sys


def main():
    p = ArgumentParser()
    p.add_argument('loc', help='Maidenhead grid or lat lon', nargs='+')
    p.add_argument('-p', '--precision', help='maidenhead precision', type=int, default=3)
    p = p.parse_args()

    if len(p.loc) == 1:  # maidenhead
        lat, lon = maidenhead.toLoc(p.loc[0])
        print(lat, lon)
    elif len(p.loc) == 2:  # lat lon
        loc = maidenhead.toMaiden(p.loc[0], p.loc[1], p.precision)
        print(loc)
    else:
        print('specify Maidenhead grid (single string) or lat lon (with space between)', file=sys.stderr)


if __name__ == '__main__':
    main()
