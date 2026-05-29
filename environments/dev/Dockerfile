FROM python:3.14.5-alpine3.23

ARG USER_ID
ARG GROUP_ID

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=core.settings.dev

RUN addgroup -g ${GROUP_ID} dev && \
    adduser -u ${USER_ID} -G dev -h /home/dev -s /bin/sh -D dev

WORKDIR /app

COPY requirements/ ./requirements/

RUN chown -R dev:dev /app

USER dev

RUN pip install --no-cache-dir -r requirements/dev.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
