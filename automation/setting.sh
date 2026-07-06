#!/bin/bash
# Setup All For Use In Production
poetry run flask --app hanger_app:create_app db-upgrade
poetry run flask --app hanger_app:create_app create-admin
poetry run flask --app hanger_app:create_app process-jobs --watch
poetry run flask --app hanger_app:create_app settings-list
poetry run flask --app hanger_app:create_app settings-set eligibility.minimum_age 21
poetry run flask --app hanger_app:create_app schedule-interview 1
poetry run flask --app hanger_app:create_app add-interview-note 1
poetry run flask --app hanger_app:create_app research-export
poetry run pytest -q
poetry run ruff check src tests