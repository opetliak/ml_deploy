FROM python:3.8.2-slim-buster
RUN useradd --create-home appuser
USER appuser

WORKDIR /home/appuser
COPY . .
RUN which python
RUN python -m pip install --upgrade pip setuptools wheel
ENV PYTHONFAULTHANDLER=1
EXPOSE 8080
CMD ["ls", "-l"]
