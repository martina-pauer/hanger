# Technical Roadmap

This roadmap converts the current product notes in `ROADMAP.md` into
implementable engineering work for `hanger_app`. It focuses on backend,
security, operations, and documentation milestones.

## 1. Controlled User Onboarding

Goal: only register users who pass a selection process.

Implementation scope:

- [x] Add an application workflow with states: `submitted`, `screening`,
  `interview`, `accepted`, `rejected`, and `invited`.
- [x] Store application answers, reviewer notes, decision timestamps, and
  reviewer user IDs.
- [x] Replace open registration with invite-only registration tied to accepted
  applications.
- [x] Add admin routes and CLI commands to review, accept, reject, and invite
  applicants.
- [x] Add audit events for application state changes.

Acceptance criteria:

- [x] A non-invited user cannot create an account.
- [x] Accepted applicants receive a single-use invitation.
- [x] Tests cover duplicate applications, rejected applications, expired
  invites, and admin-only decisions.

## 2. Per-Installation Requirements

Goal: support different eligibility rules and operating limits for each
deployed server.

Implementation scope:

- [x] Introduce an `installation_settings` table for onboarding rules,
  eligibility criteria, limits, and branding.
- [x] Move server-specific values out of source code into environment variables
  or database-backed settings.
- [x] Validate required production settings during application startup.
- [x] Add CLI support for reading and updating safe settings with
  `settings-list`, `settings-get`, and `settings-set`.
- [x] Document required configuration in `README.md`.

Acceptance criteria:

- [x] Each deployment can define its own eligibility rules without code changes.
- [x] Missing production configuration fails fast with a clear error.
- [x] Tests verify default settings, overrides, and invalid configuration.

## 3. Interview and Research Pipeline

Goal: manage interviews with possible future users and convert research into
actionable product signals.

Implementation scope:

- [x] Add applicant interview scheduling fields: contact method, preferred
  times, assigned interviewer, and status.
- [x] Add interview notes with structured categories: motivation, fit, risks,
  and follow-up actions.
- [x] Add privacy controls so only admins or assigned interviewers can read
  interview notes.
- [x] Add aggregate exports for research metrics without exposing sensitive
  notes.

Acceptance criteria:

- [x] Interview notes are access-controlled and audited.
- [x] Admins can list applicants by interview status.
- [x] Research exports exclude private free-text notes by default.

## 4. Funding and Operations Readiness

Goal: prepare the project for external funding, sponsorship, or structured
collaboration.

Implementation scope:

- [x] Add operational metrics: registered users, active users, applications by
  status, invitation conversion, and message/job health.
- [x] Add CLI reporting using the existing `/health/live` and `/health/ready`
  foundations as operational context.
- [x] Improve logging around authentication, onboarding, background jobs, and
  interview decisions.
- [x] Add data retention guidance for applications, interview notes, recovery
  tokens, and invitations.
- [x] Add backup and restore documentation for SQLite deployments.

Acceptance criteria:

- [x] Maintainers can generate a funding-ready usage report without direct
  database inspection.
- [x] Sensitive user data is excluded from public or sponsor-facing exports.
- [x] Backup and restore steps are documented for a local SQLite database.

## Cross-Cutting Engineering Priorities

- Security: preserve invite token single-use semantics, role-based access
  control, audit logs, and upload authorization.
- Testing: keep coverage above the CI threshold and add route/service tests for
  every onboarding decision path.
- Migrations: add schema changes only through numbered files in
  `src/hanger_app/migrations/`; never rewrite applied migrations.
- Documentation: update `AGENTS.md`, `README.md`, and deployment notes whenever
  commands, configuration, or workflows change.
- Observability: prefer structured logs and explicit health checks over silent
  failures.

## Suggested Implementation Order

1. [x] Add application and invitation schema.
2. [x] Implement repository and service layer for application decisions.
3. [x] Add admin CLI commands and protected admin routes.
4. [x] Disable open registration when invite-only mode is enabled.
5. [x] Add installation settings and production validation.
6. [x] Add interview notes and access controls.
7. [x] Add reporting commands and sanitized exports.
8. [x] Document deployment, backup, restore, and operational workflows.

## Next Technical Work

- Add actual retention cleanup commands with dry-run support.
- Add scheduled backup automation examples for the target hosting environment.
- Add an admin UI for operational reports if maintainers need browser access.
- Add richer activity metrics once the schema tracks successful login timestamps.
