coverage:
	coverage run -m unittest discover -s tests -t .
	coverage report -m
	@coverage html
	@open ./.artifacts/coverage_report_html/index.html
.PHONY: coverage

test:
	python -m unittest discover -s tests -t . -v
.PHONY: test
