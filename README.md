# Entrega1Ruiz
Primera entrega proyecto final CoderHouse

Pasos a realizar:

Paso 1: clonar el proyecto.

Paso 2: instalar los aplicativos y dependencias, haciendo uso de requirement.txt

Paso 3: crear base de datos en postgresql

paso 4: modificar los datos de acceso a la base de datos ingresando a la siguiente ruta: desafio1CH/desafio1CH/settings/local.py

    default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'BBDD_Name',  <!--Colocar el nombre de la base de datos-->
        'USER': 'BD_User', <!--Colocar el nombre del usuario-->
        'PASSWORD': 'BD_Password', <!--Colocar la contraseña elegida-->
        'HOST': 'localhost',
        'PORT': '5432',
