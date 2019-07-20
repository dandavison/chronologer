EXECUTABLES_DIRECTORY := ./executables
HYPERFINE_OUTPUT := ./hyperfine-output.json
HYPERFINE_PROCESSED_OUTPUT := ./hyperfine-processed-output.json
BENCHMARK_TASK := ./benchmark
BRANCH := master

build:
	./build-commits.sh $(BRANCH) $(EXECUTABLES_DIRECTORY)


benchmark:
	./benchmark-commits.py $(BENCHMARK_TASK) $(EXECUTABLES_DIRECTORY) $(HYPERFINE_OUTPUT)


process:
	./transform-benchmark-data.py < $(HYPERFINE_OUTPUT) > $(HYPERFINE_PROCESSED_OUTPUT)
