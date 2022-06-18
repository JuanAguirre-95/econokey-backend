FROM python:3.10.4-slim
RUN mkdir /app
COPY /app /app
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]