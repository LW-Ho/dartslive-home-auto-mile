FROM python:3.8-alpine

USER root

WORKDIR /dartslive
COPY . /dartslive/

RUN pip install -r requirement.txt

CMD ["python", "main.py"]