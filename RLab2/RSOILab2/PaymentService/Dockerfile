FROM python

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY / /RSOILab2/
WORKDIR /RSOILab2

CMD ["python3", "main.py"]