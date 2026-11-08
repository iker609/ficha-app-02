# Ficha de la aplicación APP-02

Programa que muestra, en diez opciones, la ficha técnica de una aplicación móvil antes de
publicarla: identificación, tamaño del APK, ingresos, versionCode, permisos, color del icono y
varias comprobaciones sobre tipos y redondeo.

**Módulo:** IC44 — Fundamentos de programación en Python  
**Unidad:** 1 — Estructura de un programa y elementos del lenguaje  
**Pareja:** 2  
**Autores:** Iker Alcolea Mateos · David Raúl Rus Almaján  

## Aplicación descrita

| Dato | Valor |
|---|---|
| Código | APP-02 |
| Nombre | Lista de la Compra |
| Paquete | es.hogar.listacompra |
| Versión | 3.0.7 |
| Tamaño del APK | 18.874.368 bytes |
| Descargas y precio | 25.400 descargas · 0.49 € |

## Ejecución desde Docker Hub

No hace falta descargar el repositorio ni tener Python instalado, solo disponer de Docker.

```bash
docker run --rm --pull always yuste135/ficha-app-02:1.0.0
```

Página de la imagen: https://hub.docker.com/r/yuste135/ficha-app-02

## Ejecución en local

Requiere Python 3.10 o superior (desarrollado y probado con Python 3.14).

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows PowerShell: .venv\Scripts\Activate.ps1
python ficha_app.py
```

## Construir la imagen con Docker

Construcción y ejecución básica en local:

```bash
docker build -t ficha-app-02 .
docker run --rm ficha-app-02
```

Construcción multiarquitectura (`amd64` y `arm64`) y subida a Docker Hub:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t yuste135/ficha-app-02:1.0.0 -t yuste135/ficha-app-02:latest --push .
```

## Integración continua (CI/CD)

El repositorio incluye un workflow en GitHub Actions (`.github/workflows/ci.yml`) que automatiza dos etapas:
1. **Comprobar (en cada push a `main`):** Instala Python, verifica que el código compila con `py_compile`, pasa el linter de estilo PEP 8 y ejecuta el programa validando las 10 opciones.
2. **Publicar (al subir una etiqueta `v*` como `v1.0.0`):** Inicia sesión de forma segura en Docker Hub utilizando secretos del repositorio, compila la imagen multiarquitectura (`linux/amd64` y `linux/arm64`) mediante QEMU y Docker Buildx, y la publica automáticamente con los tags de la versión y `latest`.

## Estructura del proyecto

```
.
├── .dockerignore
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── ficha_app.py
```
