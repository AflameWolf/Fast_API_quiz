FROM python:3.11


RUN mkdir /fast_api

WORKDIR /fast_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn client_api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000


