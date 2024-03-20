FROM python:3.8

COPY requirements.txt .
RUN pip install pip --upgrade && pip install -r requirements.txt
EXPOSE 8001
CMD ["gunicorn", "main:app" "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8001"]