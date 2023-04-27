FROM python:3.8.2-slim-buster
RUN useradd --create-home appuser
USER appuser

WORKDIR /home/appuser
RUN python -m pip install --upgrade pip setuptools wheel
COPY . .
ENV PYTHONFAULTHANDLER=1
EXPOSE 8080
CMD ["python", "-m" , "http.server", "8080"]
