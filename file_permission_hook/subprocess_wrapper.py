import subprocess


def git_wrapper(path: str) -> str:
    # TODO: This is not enough. We need to check if the return code is non-zero,
    #       and act accordingly. In addition, we need to decide what to do with
    #       stderr if that happens.
    subp = subprocess.run(
        ["git", "status", "--porcelain=v2", "-z", "--", path],
        capture_output=True,
        encoding="UTF-8",
    )
    return subp.stdout
