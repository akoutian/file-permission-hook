# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import argparse

from src import subprocess_wrapper
from typing import List


def fix(mode: int, path: str) -> bool:
    if int(mode[0]) % 2 != 0:
        print(f"file '{path}' has executable bit set for user, running 'chmod -x' ...")
        subprocess_wrapper.chmod_wrapper(path)
        return True

    return False


def check(paths: List[str]) -> int:
    for path in paths:
        git_status = subprocess_wrapper.git_wrapper(path)
        stat = subprocess_wrapper.stat_wrapper(path)

        if git_status:
            mode = git_status.split(" ")[4][-3:]
            if fix(mode, path):
                return True

        if stat:
            if fix(stat, path):
                return True

    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")

    return check(parser.parse_args().paths)


if __name__ == "__main__":
    exit(main())
