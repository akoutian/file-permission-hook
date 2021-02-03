import sys
import argparse

from file_permission_hook.subprocess_wrapper import git_wrapper

from typing import Optional, Sequence, List


def check_files(paths: List[str]) -> int:
    for path in paths:
        git_output = git_wrapper(path)
        print(git_output)
    return False


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*")

    return check_files(parser.parse_args().filenames)


if __name__ == "__main__":
    exit(main())
