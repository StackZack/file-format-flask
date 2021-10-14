# File Format Flask

A sample Flask API that shows how to read a variety of file formats in Python.

## Environment Setup

```bash
cp sampledotenv.env .env  # Set up env variables
pip install -r requirements.txt  # Install required packages
```

## How To Run

### Via Command Line

```bash
flask run
```

### Via Docker

```bash
docker build -t file-format-flask .  # Build docker image
docker run --publish 5000:5000 file-format-flask  # Run docker container
```

## How To Test

```bash
pytest tests/
```

## REST Endpoints
|URL|Method|
|---|------|
|csv/read|GET|
|json/read|GET|
|avro/read|GET|
|parquet/read|GET|
|orc/read|GET|

## To-Do List
1. Add routes and controllers for Protocol Buffers
