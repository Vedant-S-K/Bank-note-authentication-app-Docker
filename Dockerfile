FROM continuumio/anaconda3:2020.11
ADD  . /usr/app/
WORKDIR /usr/app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
