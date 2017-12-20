from python:3.6.2
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
RUN mkdir -p /home/flask/app/web
WORKDIR /home/flask/app/web
COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt
# COPY . /home/flask/app/web
RUN chown -R flask:flaskgroup /home/flask
USER flask
ENTRYPOINT ["/usr/local/bin/gunicorn", "--bind", ":8000", "linode:app", "--reload"]
