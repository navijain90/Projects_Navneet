FROM python:2.7
MAINTAINER Navneet Jain "jain.navi90@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["webservice.py"]
