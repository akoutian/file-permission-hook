#!/bin/python

import sys


def main():
    print("argc: %d" % len(sys.argv))
    print("argv: %s" % sys.argv)

    exit(0)


if __name__ == "__main__":
    main()
