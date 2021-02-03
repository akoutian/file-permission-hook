import subprocess


def git_wrapper(path):
    subp = subprocess.run(
        ["git", "status", path, "--porcelain=v2", "-z"],
        capture_output=True,
        encoding="UTF-8",
    )
    return subp.stdout
