FROM tiangolo/uvicorn-gunicorn-fastapi

WORKDIR /fastapi-rf-clf

COPY . .

RUN pip install --no-cache-dir scikit-learn==1.3.2

EXPOSE 5000

CMD ["/usr/local/bin/python", "main.py"]
