FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./botaem /app
COPY ../Hack-mts/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python" ,"manage.py", "runserver","0.0.0.0:8000"]