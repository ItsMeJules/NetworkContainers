FROM python:latest

WORKDIR /scripts
COPY scripts/ .

RUN pip install redis pymongo

RUN chmod +x main.py

ENTRYPOINT ["python3", "-u", "main.py"]