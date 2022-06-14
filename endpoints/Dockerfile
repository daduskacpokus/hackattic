FROM python:3.7-alpine
WORKDIR /app
ADD . /app
RUN apk add --update py-pip && pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "-m", "flask", "run", "--host=0.0.0.0" ]
