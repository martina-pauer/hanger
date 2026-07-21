#!/bin/bash
# Get backup date
date=""
echo "Input date to restore (year, month, day, hour, minutes, seconds): "
read date
# Restore From That Backup Date
cp "backups/hanger-$date.sqlite3" "$HANGER_DB_PATH"
poetry run flask --app hanger_app:create_app db-upgrade