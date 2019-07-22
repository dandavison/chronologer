import os
import sys
from typing import Optional

from chronologer import git
from chronologer import subprocess
from chronologer.config import config
from chronologer.typing import CommitHash
from chronologer.typing import Path


def get_executable(commit: CommitHash) -> Optional[Path]:
    path = _get_executable_path(commit)
    if not os.path.exists(path):
        try:
            _build(commit)
        except subprocess.CalledProcessError as exc:
            print(exc, file=sys.stderr)
            return None
    return path


def _get_executable_path(commit: CommitHash) -> Path:
    return os.path.join(config.executables_dir, commit)


def _build(commit: CommitHash) -> None:
    git.assert_clean()
    with git.checkout(commit):
        subprocess.check_call(config.build_command.format(commit=commit).split())
        subprocess.check_call(["cp", config.built_executable, _get_executable_path(commit)])
