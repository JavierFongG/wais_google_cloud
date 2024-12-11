FROM python:3.11
LABEL authors="javi.fong"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV APP_HOME=/root
WORKDIR $APP_HOME
COPY /src $APP_HOME/backend

# remove this line in PROD environment
# COPY ./serviceAccountKey.json /serviceAccountKey.json

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]