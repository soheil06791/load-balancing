FROM python:3.10-alpine
WORKDIR /api
RUN apk update \
    && apk add build-base
COPY . .
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/sh", "/api/runner.sh"]

