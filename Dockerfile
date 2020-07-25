FROM python:3
ENV PYTHONBUFFERED 1
ENV COMPOSE_CONVERT_WINDOWS_PATHS=1 
ENV POSTGRES_HOST_AUTH_METHOD=trust
RUN mkdir /test_project
WORKDIR /test_project
COPY ./test_project /test_project
CMD [ "sh", "-c", "pip install -r requirements.txt"]