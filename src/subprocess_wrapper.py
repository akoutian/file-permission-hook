# SPDX-License-Identifier: GPL-3.0-or-later

import subprocess


def git_wrapper(path: str) -> str:
    subp = subprocess.run(
        ["git", "status", "--porcelain=v2", "-z", "--", path],
        capture_output=True,
        encoding="UTF-8",
    )

    if subp.returncode != 0:
        raise RuntimeError(subp.stderr)

    return subp.stdout


def stat_wrapper(path: str) -> str:
    subp = subprocess.run(
        ["stat", "-c", "%a", path],
        capture_output=True,
        encoding="UTF-8",
    )

    if subp.returncode != 0:
        raise RuntimeError(subp.stderr)

    return subp.stdout


def chmod_wrapper(path: str):
    subp = subprocess.run(
        ["chmod", "-x", path],
        capture_output=True,
        encoding="UTF-8",
    )

    if subp.returncode != 0:
        raise RuntimeError(subp.stderr)

    return
