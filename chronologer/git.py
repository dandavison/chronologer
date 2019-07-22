import os
import subprocess
import sys
from contextlib import contextmanager


@contextmanager
def checkout(commit):
    original_commit = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip()
    subprocess.check_call(["git", "checkout", "-q", commit])
    try:
        yield
    finally:
        subprocess.check_call(["git", "checkout", "-q", original_commit])


def get_git_dir():
    return os.path.join(
        subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode("utf-8").strip(),
        ".git",
    )


def assert_clean():
    try:
        subprocess.check_call(["git", "diff", "--quiet"])
        subprocess.check_call(["git", "diff", "--cached", "--quiet"])
        assert not subprocess.check_output(
            ["git", "ls-files", "--other", "--exclude-standard", "--directory"]
        )
    except (subprocess.CalledProcessError, AssertionError):
        print(
            "Git working directory is not clean: "
            "please commit/stash changes and uncommitted files."
        )
        sys.exit(1)
