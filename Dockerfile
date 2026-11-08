FROM python:3.14-slim

LABEL org.opencontainers.image.title="Ficha técnica de una aplicación móvil"
LABEL org.opencontainers.image.authors="Iker Alcolea Mateos, David Raúl Rus Almaján"
LABEL org.opencontainers.image.source="https://github.com/iker609/ficha-app-02"

WORKDIR /app

COPY ficha_app.py .

CMD ["python", "ficha_app.py"]
