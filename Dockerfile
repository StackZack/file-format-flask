FROM python:3.9-slim-buster

WORKDIR /app

#Copy over requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#Copy over application files
COPY sampledotenv.env .env
COPY file_format_flask file_format_flask

#Run application
CMD ["flask", "run", "--host=0.0.0.0"]
