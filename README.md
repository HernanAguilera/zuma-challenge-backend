# Challenge Python Backend

## Preparación del entorno

1. Clonar el proyecto
```
git clone git@github.com:HernanAguilera/zuma-challenge-backend.git
```
2. entrar en el directorio del proyecto
```
cd zuma-challenge-backend
```
3. Instalar las librerias python requeridas
```
pip install -r requirements.txt
```
1. Ejecutar los contenedores docker (esto instala postgresql)
```
docker-composer up -d
```

## Instalación

1. Ejecutar las migraciones
```
python manage.py migrate
```

## Ejecutar el proyecto

1. Correr el servicor de prueba

```
python manage.py runserver
```

2. Abrir en el navegador la dirección:

```
http://127.0.0.1:8000/
```