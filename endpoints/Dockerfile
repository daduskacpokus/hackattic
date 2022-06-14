FROM python:3.7-alpine
WORKDIR /app
ADD . .
RUN apk add py-pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "/usr/local/bin/python" ]
CMD [ "-m", "flask", "run", "--host=0.0.0.0" ]
