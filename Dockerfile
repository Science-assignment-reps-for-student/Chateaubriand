FROM python:3.8.1
MAINTAINER mallycrip "migsking@naver.com"

COPY . .
WORKDIR .

RUN mkdir logs
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["-m","chateaubriand"]

EXPOSE 5000
