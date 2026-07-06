# Hanger

Hanger is an interview-gated social application built with Flask. It includes
registration, login, password recovery, persistent invitations, messaging,
posts, validated image uploads, per-installation settings, applicant interviews,
and retryable delivery jobs.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
poetry run flask --app hanger_app:create_app run --debug
```

Development data is stored under `instance/`. Production requires
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION`, and
`HANGER_MAX_UPLOAD_BYTES`. Configure SMTP or Twilio credentials before
processing delivery jobs. SQLite and uploaded files must live on the same
persistent volume; this deployment profile is intended for one application host.

## Common commands

```bash
poetry run flask --app hanger_app:create_app db-upgrade
poetry run flask --app hanger_app:create_app create-admin
poetry run flask --app hanger_app:create_app process-jobs --watch
poetry run flask --app hanger_app:create_app settings-list
poetry run flask --app hanger_app:create_app settings-set eligibility.minimum_age 21
poetry run flask --app hanger_app:create_app submit-application
poetry run flask --app hanger_app:create_app schedule-interview 1
poetry run flask --app hanger_app:create_app add-interview-note 1
poetry run flask --app hanger_app:create_app research-export
poetry run flask --app hanger_app:create_app operations-report
poetry run pytest -q
poetry run ruff check src tests
```

Schema changes belong in numbered SQL files under
`src/hanger_app/migrations/`. Development applies them automatically;
production must run `db-upgrade` once before web workers start. Health checks
are available at `/health/live` and `/health/ready`.

## Configuration and workflows

Per-installation settings are stored in SQLite and managed with
`settings-list`, `settings-get`, and `settings-set`. Supported settings include
`branding.site_name`, `branding.support_contact`, `branding.logo_url`,
`eligibility.minimum_age`, `eligibility.allowed_contact_kinds`, and
`eligibility.application_prompt`.

Interview workflow commands let admins schedule applicant interviews, assigned
interviewers record structured notes, and maintainers export aggregate research
metrics without exposing private note text by default.

`operations-report` emits sanitized operational metrics for maintainers:
registered users, active users, applications by status, invitation conversion,
job health, content totals, audit event count, and retention follow-up counts.
The report intentionally excludes usernames, contact addresses, job payloads,
recovery tokens, and interview note text.

## Backup, restore, and retention

Back up SQLite with the database online using SQLite's backup command:

```bash
mkdir -p backups
sqlite3 "$HANGER_DB_PATH" ".backup 'backups/hanger-$(date +%Y%m%d%H%M%S).sqlite3'"
```

Restore only after stopping web and worker processes:

```bash
cp backups/hanger-YYYYMMDDHHMMSS.sqlite3 "$HANGER_DB_PATH"
poetry run flask --app hanger_app:create_app db-upgrade
```

Keep uploaded files backed up with the same schedule as the database so
attachment references stay consistent. Operational retention targets are:
review closed applications after 90 days, review interview notes after 180 days,
clear expired password recovery tokens, and clean expired unused invitations.
Use `operations-report` to identify records that need review before deletion.
