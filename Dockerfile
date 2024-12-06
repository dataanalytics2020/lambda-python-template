FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/

CMD ["src.handlers.main.lambda_handler"] 