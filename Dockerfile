FROM python:3.7

COPY ./ /app
WORKDIR /app

RUN python3 -m ensurepip

RUN pip install pipenv 
RUN pipenv install --dev --system --deploy

ENTRYPOINT ["python"]
CMD ["manage.py"]
