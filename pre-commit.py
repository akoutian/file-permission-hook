#!/bin/python

import sys


def main():
    print(f"argc: {len(sys.argv)}")
    print(f"argv: {sys.argv}")

    exit(0)


if __name__ == "__main__":
    main()