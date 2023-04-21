import sys
import argparse
from typing import List

from src import subprocess_wrapper


def check(paths: List[str]) -> int:
    for path in paths:
        status = subprocess_wrapper.git_wrapper(path)

        if not status:
            return False

        mode = status.split(" ")[4][-3:]

        if int(mode[0]) % 2 != 0:
            print(
                f"staged file '{path}' has executable bit set for user, running 'chmod -x' ..."
            )
            subprocess_wrapper.chmod_wrapper(path)
            return True

    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")

    return check(parser.parse_args().paths)


if __name__ == "__main__":
    exit(main())
