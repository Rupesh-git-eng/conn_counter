FROM registry.access.redhat.com/ubi9/ubi:9.6
RUN  dnf install -y python3.12

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python3.12", "app.py"]
