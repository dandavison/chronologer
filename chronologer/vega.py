import json
import os

from jinja2 import Template

from chronologer.config import config


def write_html():
    html_file = os.path.join(os.path.dirname(__file__), "..", "templates", "index.html")
    with open(html_file) as fp:
        html_template = Template(fp.read())
    if not config.dry_run:
        boxplot_spec = json.dumps(_get_boxplot_spec(), indent=2)
        with open(config.html_output_file, "w") as fp:
            fp.write(html_template.render(boxplot_spec=boxplot_spec))


def _get_boxplot_spec():
    with open(config.combined_benchmark_file) as fp:
        values = json.load(fp)
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
        "data": {"values": values},
        "mark": {"type": "boxplot", "extent": "min-max", "size": 5},
        "width": 1400,
        "height": 500,
        "encoding": {
            "y": {"field": "time", "type": "quantitative", "axis": {"title": "Time"}},
            "x": {
                "field": "commit",
                "type": "ordinal",
                "axis": {"title": "Commit", "labels": False, "ticks": False},
            },
            "tooltip": {"field": "message", "type": "ordinal", "aggregate": "min"},
        },
    }
