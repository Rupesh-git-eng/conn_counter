FROM registry.access.redhat.com/ubi9/ubi

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python", "app.py"]
