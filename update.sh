#!/bin/bash
# Run python scripts
python3 Download\ JSON.py
python3 Compile\ Schedule.py

# Pretty-print JSON objects
python3 -m json.tool players.json > players_temp.json
python3 -m json.tool schedule.json > schedule_temp.json
cat players_temp.json > players.json
cat schedule_temp.json > schedule.json
rm players_temp.json
rm schedule_temp.json

# Deployment to cPanel
git add .
# Add date-time to commit message
COMMIT_DATE=$(date)
git commit -m "Auto-commit: $COMMIT_DATE"
git push
