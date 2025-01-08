FROM python:3.8

WORKDIR /hello_app

COPY printer.py /hello_app

RUN pip install flask

EXPOSE 5000

CMD ["python", "/hello_app/printer.py"]

