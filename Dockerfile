FROM python:3.9.0
# If needed you can use the official python image (larger memory size)
#FROM python:3.9.0

RUN mkdir /app/
WORKDIR /app

COPY src/TestCalculationService src/TestCalculationService
COPY requirements.txt ./
COPY pyproject.toml ./
COPY README.md ./
RUN pip install -r requirements.txt && pip install ./

ENTRYPOINT ["python3", "src/TestCalculationService/TestService.py"]