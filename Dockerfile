# Dockerfile, Image, Container
FROM python:3.8.10

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "entry:app", "--host", "das", "--port", "8080"]
# CMD ["/bin/bash", "-c", "echo alembic upgrade heads; echo uvicorn entry:app --host das --port 8080"]
