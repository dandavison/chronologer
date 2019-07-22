import subprocess
from dataclasses import dataclass
from typing import List

import yaml

from chronologer.typing import CommitHash


@dataclass
class Config:
    benchmarks_dir: str = ""
    benchmark_runs: int = -1
    benchmark_task: str = ""
    build_command: str = ""
    built_executable: str = ""
    combined_benchmark_file: str = ""
    dry_run: bool = False
    executables_dir: str = ""
    html_output_file: str = "index.html"
    revision_range: str = ""

    def populate_from_file(self, path: str, opt: dict):
        with open(path) as fp:
            for key, val in yaml.safe_load(fp).items():
                assert key in self.__dict__
                self.__dict__[key] = val
        self.dry_run = opt["--dry-run"]

    def get_commits(self) -> List[CommitHash]:
        """
        List of commits to benchmark.
        """
        return [
            line.decode("utf-8")
            for line in subprocess.check_output(
                ["git", "rev-list", self.revision_range]
            ).splitlines()
        ]


config = Config()
