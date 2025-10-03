FROM registry.redhat.io/rhel9/python-312

WORKDIR /app
COPY app.py /app/

EXPOSE 8080

CMD ["python", "app.py"]
