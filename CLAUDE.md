# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Package Discovery is a Python library for package discovery based on Setuptools. The main functionality provides filtering of duplicate package paths and identifies root-only packages from nested package hierarchies.

## Development Environment Setup

Uses `uv` for dependency management. Install development dependencies:
```bash
uv sync
```

## Common Development Commands

### Testing
- `uv run pytest` - Run fast tests (excludes @pytest.mark.slow tests)
- `uv run inv test.all` - Run all tests including slow ones
- `uv run inv test.coverage` - Run tests with coverage report
- `uv run pytest tests.test_packagediscovery` - Run specific test module

### Code Quality
- `uv run inv style` - Format code with docformatter and Ruff
- `uv run inv style --check` - Check formatting without making changes
- `uv run inv lint` - Run fast linting (xenon, ruff, bandit, dodgy, flake8, pydocstyle)
- `uv run inv lint.deep` - Run comprehensive linting (mypy, Pylint, semgrep)

### Building
- `uv run inv dist` - Build source and wheel packages into dist/ directory

### Cleanup
- `uv run inv clean` - Clean all generated files

## Architecture

### Core Components

- `packagediscovery/packages.py` - Contains `Packages`, `RootOnly`, and `PairPackage` classes for filtering duplicate package paths
- `packagediscovery/setuptools.py` - Contains `Setuptools` class that wraps setuptools discovery APIs

### Key Classes

- `Packages`: Main class that takes a list of package names and provides `list_roots_only` property to get filtered root packages
- `RootOnly`: Internal filtering logic that removes sub-packages when parent packages are present
- `PairPackage`: Helper class for comparing package relationships (parent/child detection)
- `Setuptools`: Wrapper around setuptools ConfigDiscovery for package discovery

## Code Standards

- Uses strict typing with mypy
- Google-style docstrings
- Line length: 119 characters
- Black formatting with Ruff linting
- Comprehensive test coverage required
- All linting tools must pass before commits

## Testing Strategy

Tests are located in `tests/` directory using pytest framework. The project has both fast and slow test markers. Test files mirror the package structure (`test_packages.py`, `test_setuptools.py`).