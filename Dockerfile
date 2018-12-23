FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install redis
CMD ["python", "app.py"]