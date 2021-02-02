import sys
import argparse

from file_permission_hook.subprocess_wrapper import git_wrapper


def check_files(args):
    for path in args.filenames:
        git_wrapper(path)
    exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*")

    return check_files(parser.parse_args())


if __name__ == "__main__":
    exit(main())
