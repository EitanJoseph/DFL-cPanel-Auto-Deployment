#!/bin/bash
python3 csv\ to\ json.py
python3 Compile\ Schedule.py
git add .
git commit -m "Auto-commit:" -m "`$commitDate`"
git push
