># 🫱 Local installation for development
## Install environment
```bash
python -m venv venv
```

## Activate environment
```bash
source venv/bin/activate
```

## Install packages
```bash
pip install --upgrade -r ./requirements.txt
```

## Start the server
```bash
uvicorn app.main:app --reload
```

> # 🫱 Run with Docker

## Create an .env file with the path of main file, for example:
```bash
APPLICATION_PATH=app.main:app
```

## Build and execute container
```bash
docker compose up --build --force-recreate
```

> # 🫱 Run with the bash script
In the file [execution.sh](./execution.sh) we can execute with two options, one locally and one with docker:

➡️ Local
```bash
bash execution.sh --local --install
bash execution.sh --local --run_books_app
```
or

```bash
bash execution.sh --local --install
bash execution.sh --local --run_todo_app
```

➡️ Container execution 
```bash
bash execution.sh --docker
```
# 🫱 API documentation
## To access the API documentation, you must access the endpoints */docs* or */redoc*