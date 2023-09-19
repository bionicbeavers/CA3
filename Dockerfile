FROM python:3.8

RUN mkdir -p /dock

WORKDIR /dock

COPY requirements.txt /dock/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /dock/

CMD ["python", "calculator.py"]