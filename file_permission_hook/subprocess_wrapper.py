import subprocess

def git_wrapper():
    subp = subprocess.run(['git', 'status', '--porcelain=v2', '-z'], capture_output=True)
    print(subp.stdout)

