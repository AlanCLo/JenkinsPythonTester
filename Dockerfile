FROM python:2.7.10

RUN mkdir -p /usr/src/blahapp
WORKDIR /usr/src/blahapp
ADD . /usr/src/blahapp
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
