# DEPRECATED: CSGO-Ping-Tester-redux

### Valve no longer provides a public-facing .json file with relay addresses to different regions since CS2 was released, therefore this project is useleess.

### A re-written version of CSGO-Ping-Tester

[![renovate: enabled](https://img.shields.io/badge/renovate-enabled-green)](https://github.com/Defirence/CSGO-Ping-Tester-redux/blob/main/renovate.json)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![.github/workflows/pylint.yml](https://github.com/Defirence/CSGO-Ping-Tester-redux/actions/workflows/pylint.yml/badge.svg?branch=dev)](https://github.com/Defirence/CSGO-Ping-Tester-redux/actions/workflows/pylint.yml)

This is the dev branch, which tracks active development.

`requirements.txt` - Contains all the `pip` packages needed to build + run the project.

`main.py` - The main "script", the core of what the script/program does.

Uses `GitHub Actions` for testing on `push` to dev/+main branch(es) in `.github/workflows/pylint.yml`

#### Linting:

Uses `pylint` for linting with GitHub Actions

#### (WIP) Testing:

Uses `pytest` for testing.
