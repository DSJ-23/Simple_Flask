FROM python:3.8.0-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

# docker build -t a_flask_python .
# docker run  -p 5000:5000 a_flask_python
# docker build -t test1 .
# docker run -d -p 5000:5000 test1
# docker run -p 5000:5000 test1
# docker images -a | grep "python"  
# docker kill $(docker ps -q)
