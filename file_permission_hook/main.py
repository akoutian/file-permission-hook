#!/usr/bin/python

import sys
import argparse

from file_permission_hook.subprocess_wrapper import git_wrapper


def check_files(paths):
    git_wrapper()
    exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*")

    args = parser.parse_args()
    print(args)

    return check_files(args)


if __name__ == "__main__":
    exit(main())
