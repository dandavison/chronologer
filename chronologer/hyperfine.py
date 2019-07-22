import json
import os
import re
import sys

from pygit2 import Repository

from chronologer.config import config
from chronologer.git import get_git_dir


def combine_benchmark_files():
    combined = {"results": []}
    for file_name in sorted(os.listdir(config.benchmarks_dir)):
        with open(os.path.join(config.benchmarks_dir, file_name)) as fp:
            data = json.load(fp)
            combined["results"].extend(data["results"])
    if not config.dry_run:
        with open(config.combined_benchmark_file, "w") as fp:
            json.dump(transform_data(combined), fp, sort_keys=True, indent=2)


def transform_data(input):
    repo = Repository(get_git_dir())
    commits = {commit.id.hex: commit for commit in repo.walk(repo.branches.get("master").target)}

    output = []
    for row in input["results"]:
        if row["command"].endswith("[ERROR]"):
            continue
        dir, commit_hash = re.match("^([^ ]+/)?([0-9a-f]+)", row["command"]).groups()
        try:
            commit = commits[commit_hash]
        except KeyError:
            print(f"Skipping commit {commit_hash}", file=sys.stderr)
            continue
        for time in row["times"]:
            output_row = row.copy()
            output_row["commit"] = f"{commit.commit_time}-{commit_hash}"
            output_row["message"] = commit.message
            del output_row["times"]
            output_row["time"] = time

            output.append(output_row)

    return output
