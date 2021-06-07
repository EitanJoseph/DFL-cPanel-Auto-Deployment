#!/bin/bash
python3 csv\ to\ json.py
python3 Compile\ Schedule.py
git add .
COMMIT_DATE=$(date)
git commit -m "Auto-commit: $COMMIT_DATE"
git push
