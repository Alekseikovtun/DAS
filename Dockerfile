# Dockerfile, Image, Container
FROM python:3.8.10-slim

WORKDIR /src

COPY . .

RUN rm -f ./.env
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["/bin/bash","-c","python migrations.py migrate && python migrations.py init-values && uvicorn entry:app --host das --port 8080"]