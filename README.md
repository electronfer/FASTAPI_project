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
SECRET_KEY=<my_secret_key_to_encrypt>
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
### To access the API documentation, you must access the endpoints */docs* or */redoc*

# 🫱 Libraries used in the application
* *fastapi:* web framework for the API building.
* *uvicorn[standard]:* ASGI server, for production.
* *sqlalchemy:* "object-relational mapping" library.
* *passlib[bcrypt]:* package to handle password hashes.
* *python-jose[cryptography]:* package to generate and verify the JWT tokens.
* *psycopg2-binary:* PostgreSQL database adapter.
* *pymssql:* SQL Server database adapter.
* *alembic:* database migration tool for usage with the SQLAlchemy Database Toolkit.


# 🫱 Commands to deploy PostgreSQL with Docker
```bash
docker pull postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker start some-postgres
docker exec -it some-postgres psql -U postgres
```
> ## *Note:* Remember create the database
# 🫱 Configurations Alembic
## [Step 1] Configure the url in the file [alembic.ini](./Alembic/alembic.ini)
```
sqlalchemy.url = postgresql://postgres:mysecretpassword@172.17.0.2:5432/todoapplicationdatabase
```
## [Step 2] Configure the [env.py](./Alembic/alembic/env.py) file
```python
import sys
sys.path.append("...")

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

# Interpret the config file for Python logging.
# This line sets up loggers basically.
#if config.config_file_name is not None:
#    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

...
```

# 🫱 Commands used with Alembic
```bash
alembic init alembic
alembic revision -m "<message>"
alembic upgrade head
alembic downgrade -1
```