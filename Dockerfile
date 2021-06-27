FROM python:3.7

COPY ./app/requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
COPY entrypoint.sh /app/

WORKDIR app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["/app/entrypoint.sh"]