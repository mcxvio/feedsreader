FROM python:3.6-alpine

COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]