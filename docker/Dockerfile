FROM neosapience/appname-worker:base

ENV PYTHONPATH=/opt/code

COPY ./worker .

EXPOSE 5000
ENTRYPOINT ["/opt/code/docker-entrypoint.sh"]
CMD [ "celery" ]
