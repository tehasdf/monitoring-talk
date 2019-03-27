FROM python
VOLUME /app
WORKDIR /app
RUN pip install flask prometheus_client uwsgi pytelegraf
