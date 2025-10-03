FROM registry.access.redhat.com/ubi8/ubi
RUN  yum install python39

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python3.9", "app.py"]
