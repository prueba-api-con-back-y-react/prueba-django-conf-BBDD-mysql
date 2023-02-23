Para ejecutar el proyecto es necesario seguir estos pasos:

1) crearse entorno virtual de python 3.10 o python 3.11 (**comprobar versión porque está con la última versión de django; comando = python --version**): python -m venv nombre
2) activarse el entorno virtual creado en el paso: .\nombre\Scripts\activate  
3) clonarse el repositorio: git clone https://github.com/prueba-api-con-back-y-react/prueba-django-conf-BBDD-mysql.git
4) instalarse los requerimientos: cd prueba   pip install -r requirements.txt

Las credenciales para el admin son: 

usuario: root
password: root

## URL DESPLIEGUE AL PAW CON BBDD MySQL

https://pruebamysql.pythonanywhere.com/

**NOTA: El error 404 es debido a que solo es una API por lo que solo devuelve respuestas HTTP tipo GET en formato JSON de las entidades Person creada en el proyecto. (/persons o /persons/id (donde id representa al identificador de la PK de la entidad Person)).

**URL DEL PAW: https://www.pythonanywhere.com/login/

**CREDENCIALES DE ACCESO AL PAW: --> usuario PAW: pruebaMySQL
                                     password PAW: prueba
