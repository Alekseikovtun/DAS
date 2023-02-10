# Dockerfile, Image, Container
FROM python:3.8.10

WORKDIR /src

COPY . .

RUN rm -f ./.env
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "migrations.py", "migrate", "&&", "uvicorn", "entry:app", "--host", "das", "--port", "8080"]