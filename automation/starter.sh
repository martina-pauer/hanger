#!/bin/bash
# Go to Repository Source Code root
cd /workspaces/hanger/src/
# Run App
poetry run flask --app hanger_app:create_app run --debug
poetry run flask --app hanger_app:create_app process-jobs --watch