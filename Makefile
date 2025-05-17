.PHONY: clear-log
clear-log:
	rm -rf ./logs
.PHONY: isort
isort:
	ruff check --select I --fix
.PHONY: check
check:
	ruff check
.PHONY: format
format:
	ruff format
.PHONY: check-fix
check-fix:format
	ruff check --fix
	ruff check --select F401 --fix --extend-exclude dummy_imports.py --extend-exclude app.py --extend-exclude ui/forms  .
.PHONY:clean
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf ./.ruff_cache
	rm -rf ./output
	rm -rf ./build
	rm -rf ./dist
	find . -maxdepth 2 -name "*.so" -delete
	find . -maxdepth 2 -name "*.c" -delete
	find . -maxdepth 2 -name "*.spec" -delete
.PHONY:build
build:clean
	python ./scripts/build.py
convert:
	./scripts/convert.sh