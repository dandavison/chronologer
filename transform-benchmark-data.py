#!/usr/bin/env python
import argparse
import json
import re
import sys

from pygit2 import Repository

parser = argparse.ArgumentParser()
parser.add_argument("git_dir", help=".git directory of git repository (to fetch commit data)")
args = parser.parse_args()

repo = Repository(args.git_dir)
commits = {
    commit.id.hex: commit for commit in repo.walk(repo.branches.get("master").target)
}

input = json.load(sys.stdin)

output = []
for row in input["results"]:
    if row["command"].endswith("[ERROR]"):
        continue
    dir, commit_hash = re.match("^([^ ]+/)?([0-9a-f]+)", row["command"]).groups()
    try:
        commit = commits[commit_hash]
    except KeyError:
        print(f'Skipping commit {commit_hash}', file=sys.stderr)
        continue
    for time in row["times"]:
        output_row = row.copy()
        output_row["commit"] = f"{commit.commit_time}-{commit_hash}"
        output_row["message"] = commit.message
        del output_row["times"]
        output_row["time"] = time

        output.append(output_row)

json.dump(output, sys.stdout, indent=2)
