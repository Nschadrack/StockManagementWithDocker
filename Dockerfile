FROM python:3.12-slim

WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# ENV POSTGRES_PORT=${POSTGRES_PORT}
# ENV POSTGRES_HOST=${POSTGRES_HOST}
# ENV POSTGRES_PASS=${POSTGRES_PASS}
# ENV POSTGRES_USER=${POSTGRES_USER}
# ENV POSTGRES_DB=${POSTGRES_DB}
# ENV SECRET_KEY=${SECRET_KEY}

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

