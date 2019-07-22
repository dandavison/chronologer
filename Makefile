check:
	flake8 chronologer
	mypy --ignore-missing-imports chronologer

test: check
	chronologer tests/chronologer.yaml
