FROM python:3.10
ADD . /code
WORKDIR /code
RUN pip3 install -r req.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]