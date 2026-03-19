FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/", "-v", "--html=reports/report.html", "--self-contained-html"]