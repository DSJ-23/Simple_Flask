FROM python:3.8.0-buster

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . /app

RUN rm *.txt
RUN rm hello.py

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

# docker container exec -it example_flask sh

# Delete all containers
# docker rm -vf $(docker ps -a -q)

# Delete all images
# docker rmi -f $(docker images -a -q)



# CMD ["python", "setup.py"]
# RUN from setup import *

# CMD ['python', 'setup.py']




# docker build -t a_flask_python .
# docker run  -p 5000:5000 a_flask_python
# docker build -t test1 .
# docker run -d -p 5000:5000 test1
# docker run -p 5000:5000 test1
# docker images -a | grep "python"  
# docker kill $(docker ps -q)
