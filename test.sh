#!/usr/bin/env bash
rm -f .coverage
echo "Running Tests..."
coverage run -a --rcfile=coverage.ini -m pytest
coverage report -m --rcfile=coverage.ini
echo "Linting..."
flake8
echo "Testing Complete"