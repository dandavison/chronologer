"""Usage: chronologer CONFIG_FILE [--dry-run]

Options:
  -h --help     Show this screen.
  --dry-run     Just print commands; don't do anything.
"""
from docopt import docopt

from chronologer.benchmark import benchmark
from chronologer.benchmark import has_benchmark
from chronologer.config import config
from chronologer.hyperfine import combine_benchmark_files
from chronologer.vega import write_html


def main():
    opt = docopt(__doc__)
    config.populate_from_file(opt["CONFIG_FILE"], opt)
    for commit in config.get_commits():
        if not has_benchmark(commit):
            benchmark(commit)
    combine_benchmark_files()
    write_html()
