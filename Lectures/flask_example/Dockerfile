FROM python:3.7

RUN mkdir /app
WORKDIR /app
COPY . /
RUN pip install -r requirements.txt

RUN ls /app/

EXPOSE 5000
CMD ["python", "/app/main.py"]