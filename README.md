Visualize changes in program benchmark timings over git commit history.

![image](https://user-images.githubusercontent.com/52205/65389080-fdaf8380-dd49-11e9-9177-9f6621cc7081.png)

This tool uses https://github.com/sharkdp/hyperfine for the benchmarking.

## Getting started

Install via
```bash
pip3 install -r requirements.txt
pip3 install .
```

First example: `chronologer tests/chronologer.yaml` and then open the produced
`tests/index.html`. For your own project, take `tests/chronologer.yaml` as a
starting point. Some hints: avoid outputs inside the repository you are trying
to profile; your to be profiled executable must be statically linked, as they
get copied into a separate output directory.
