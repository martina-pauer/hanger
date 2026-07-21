#!/bin/bash
mkdir -p backups
sqlite3 "$HANGER_DB_PATH" ".backup 'backups/hanger-$(date +%Y%m%d%H%M%S).sqlite3'"