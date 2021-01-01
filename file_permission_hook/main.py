#!/usr/bin/python

import sys
import argparse


def check_files(paths):
    exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*")

    args = parser.parse_args()
    print(args)

    return check_files(args)


if __name__ == "__main__":
    exit(main())
