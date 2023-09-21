FROM python:3.8

RUN mkdir -p /dock

WORKDIR /dock

COPY requirements.txt /dock/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /dock/

# Expose port 5000
EXPOSE 5000

CMD ["python", "calculator.py"]
