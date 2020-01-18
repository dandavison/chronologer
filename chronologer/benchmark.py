import os
from pathlib import Path

from chronologer import subprocess
from chronologer.config import config
from chronologer.executable import get_executable
from chronologer.typing import CommitHash


def benchmark(commit: CommitHash):
    executable = get_executable(commit)
    if not executable:
        return
    Path(config.benchmarks_dir).mkdir(parents=True, exist_ok=True)
    subprocess.check_call(
        [
            "hyperfine",
            config.benchmark_task.format(executable=executable),
            "--runs",
            f"{config.benchmark_runs}",
            "--warmup",
            f"{config.warmup}",
            "--export-json",
            _get_benchmark_file(commit),
            "--ignore-failure",
        ]
    )


def has_benchmark(commit):
    return os.path.exists(_get_benchmark_file(commit))


def _get_benchmark_file(commit):
    return os.path.join(config.benchmarks_dir, commit)
