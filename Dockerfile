FROM registry.access.redhat.com/ubi8/ubi

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python3.9", "app.py"]
