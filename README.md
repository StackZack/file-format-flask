# File Format Flask

A sample Flask API that shows how to read a variety of file formats in Python.

## Environment Setup

```bash
cp sampledotenv.env .env  # Set up env variables
pip install -r requirements.txt  # Install required packages
```

## How To Run

```bash
flask run
```

## REST Endpoints
|URL|Method|
|---|------|
|csv/read|GET|
|json/read|GET|

## To-Do List
1. Add routes and controllers for a variety of formats
   1. Protocol Buffers
   2. Parquet
   3. ORC
2. Add unit tests for endpoints that are added
