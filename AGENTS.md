# Repository Guidelines

## Project Structure & Module Organization

Python application code lives in `src/hanger_app/`. `__init__.py` owns the Flask
factory and CLI commands, `routes.py` handles HTTP, `services.py` contains use
cases, and `repositories.py` isolates SQLite access. Versioned schema files live
in `src/hanger_app/migrations/`; Jinja templates live in
`src/hanger_app/templates/`. Compatibility entry points are `src/hanger.py` and
`src/loader.py`. Tests live in `tests/`. Agent instructions are stored in
`.agents/skills/`, with installed versions recorded in `skills-lock.json`.

## Build, Test, and Development Commands

Create an isolated environment before installing dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
```

Run the main application from the repository root:

```bash
poetry run flask --app hanger_app:create_app run --debug
```

Use `poetry run flask --app hanger_app:create_app db-upgrade` to apply
migrations and `process-jobs --watch` to process queued deliveries. Use
`settings-list`, `settings-get`, and `settings-set <key> <json-value>` for
per-installation settings. Use `submit-application`, `review-applications`,
`schedule-interview`, `add-interview-note`, `research-export`, and
`operations-report` for onboarding, interview, research, and operational
workflows. Use `retention-cleanup` first as a dry-run; add `--apply` only after
reviewing the counts.

## Coding Style & Naming Conventions

Use four-space indentation and follow PEP 8. Name functions and variables with
`snake_case`, classes with `PascalCase`, and constants with `UPPER_SNAKE_CASE`.
Add type hints to public methods and route return values. Keep Flask route
handlers small; move reusable behavior into `src/hanger_app/services.py`. Prefer
`pathlib.Path` and repository-relative paths. Never interpolate user input into
SQL or HTML.

## Testing Guidelines

Add new tests under `tests/`, mirroring the source layout. Name files
`test_<module>.py` and test functions `test_<behavior>()`. Run:

```bash
poetry run python -m compileall -q src tests
poetry run ruff check src tests
poetry run pytest -q
```

Route changes should cover successful requests, authorization failures, invalid
data, and expected status codes. Reporting exports must avoid usernames,
contact addresses, recovery tokens, job payloads, and private interview note
text.

## Commit & Pull Request Guidelines

History uses short, imperative, title-cased subjects such as
`Fix Login Validation` or `Add User Loader`. Keep each commit focused. Pull
requests must explain the problem, root cause, user impact, and validation
performed. Link relevant issues and include screenshots for changes under
`pages/`. Do not mix generated files, credentials, local databases, or unrelated
refactors into a PR.
