# 
FROM python:3.9

# 
WORKDIR /code/

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code/

# 
CMD uvicorn ${APPLICATION_PATH} --host 0.0.0.0 --port 80

# docker compose up --build --force-recreate fastapi