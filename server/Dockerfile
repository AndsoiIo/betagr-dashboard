FROM python:3.7

WORKDIR /server/

EXPOSE 5000
RUN apt-get update && apt-get -y install gcc

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /server/

CMD [ "python", "app.py" ]