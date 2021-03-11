import sys
import argparse

from file_permission_hook.subprocess_wrapper import git_wrapper

from typing import Optional, Sequence, List


def is_something_wrong(paths: List[str]) -> int:
    for path in paths:
        git_output = git_wrapper(path)
        print(git_output)
    # true == 1 thereby pre-commit will see it as failed
    return True


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")

    return is_something_wrong(parser.parse_args().paths)


if __name__ == "__main__":
    exit(main())
