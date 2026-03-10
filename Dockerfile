FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python db/init_db.py

CMD ["python","app/app.py"]