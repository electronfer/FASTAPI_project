#!/bin/bash
# bash execution --local
# bash execution --docker
if [ "$1" == "--local" ]; then
python -m venv venv
source ./venv/bin/activate
pip install --upgrade -r ./requirements.txt
uvicorn app.main:app --reload
fi

if [ "$1" == "--docker" ]; then
docker compose up --build --force-recreate
fi
