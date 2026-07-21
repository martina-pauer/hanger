#!/bin/bash
# Keep Uploaded Files Backed Up
poetry run flask --app hanger_app:create_app retention-cleanup
poetry run flask --app hanger_app:create_app retention-cleanup --apply