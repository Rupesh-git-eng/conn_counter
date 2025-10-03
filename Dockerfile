FROM registry.redhat.io/ubi9

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python", "app.py"]
