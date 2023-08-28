> # Local installation
## Install environment
```bash
python -m venv venv
```

## Activate environment
```bash
source venv/bin/activate
```

# Install packages
```bash
pip install --upgrade -r ./requirements.txt
```

# Start the server
```bash
uvicorn app.main:app --reload
```

> # Run with Docker
## Build and execute container
```bash
docker compose up --build --force-recreate
```