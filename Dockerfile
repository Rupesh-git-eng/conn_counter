FROM registry.redhat.io/rhel8/python-39:latest

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python", "app.py"]
