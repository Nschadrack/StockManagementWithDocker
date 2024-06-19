FROM python:3.12-slim

WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]

