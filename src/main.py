import sys
import argparse
from typing import List

from src import subprocess_wrapper


def split_git_output(output: str) -> List[str]:
    # TODO: what if git output is empty?
    output_split = output.split("\0")
    for line in output_split:
        print(line)
    return output_split


def is_something_wrong(paths: List[str]) -> int:
    for path in paths:
        git_output = subprocess_wrapper.git_wrapper(path)
        split_git_output(git_output)
    # true == 1 thereby pre-commit will see it as failed
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")

    return is_something_wrong(parser.parse_args().paths)


if __name__ == "__main__":
    exit(main())
