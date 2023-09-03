#!/bin/bash
# bash execution.sh --local --install
# bash execution.sh --local --run_books_app
# bash execution.sh --local --run_todo_app
# bash execution.sh --local --run_alembic_app
# bash execution.sh --docker
# Define the Help function
display_help() {
    echo "Usage: bash execution.sh [options]"
    echo "Options:"
    echo "  -h, --help -> Display this help message"
    echo "  --local --install -> Set the environment to run the application"
    echo "  --local --run_books_app  -> Run the books app locally"
    echo "  --local --run_todo_app  -> Run the todo app locally"
    echo "  --local --run_alembic_app  -> Run the alembic app locally"
    echo "  --docker -> Build and execute the Docker container"
}
# Check if the user specified the help option
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    display_help
    exit 0
fi

if [ "$1" == "--local" ]; then

if [ "$2" == "--install" ]; then
python -m venv venv
source ./venv/bin/activate
pip install --upgrade -r ./requirements.txt
fi

if [ "$2" == "--run_books_app" ]; then
source ./venv/bin/activate
uvicorn app.main:app --reload
fi

if [ "$2" == "--run_todo_app" ]; then
source ./venv/bin/activate
uvicorn TodoApp.main:app --reload
fi

if [ "$2" == "--run_alembic_app" ]; then
source ./venv/bin/activate
uvicorn Alembic.main:app --reload
fi

fi

if [ "$1" == "--docker" ]; then
docker compose up --build --force-recreate
fi