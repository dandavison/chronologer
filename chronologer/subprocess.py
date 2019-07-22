import subprocess
from subprocess import CalledProcessError  # noqa
from typing import List

from .config import config


def check_call(args: List[str], **kwargs):
    if config.dry_run:
        print(" ".join(args))
    else:
        subprocess.check_call(args, **kwargs)


def check_output(args: List[str], **kwargs):
    if config.dry_run:
        print(" ".join(args))
    else:
        subprocess.check_output(args, **kwargs)
