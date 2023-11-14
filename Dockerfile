FROM python:3.11-alpine
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
