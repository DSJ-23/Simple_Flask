FROM python:3.8.0-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

# CMD ['python3', 'main.py']

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

# docker build -t a_flask_python .
# docker run -p 5000:5000 a_flask_python
# docker images -a | grep "python"  
