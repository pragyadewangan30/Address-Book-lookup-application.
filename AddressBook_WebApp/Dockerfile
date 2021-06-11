FROM python:3.9.0

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./Address_Book_WebApp.py" ]