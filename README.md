# test-ego
Api's y web mobile de ejemplo de muestra de productos.

# Tecnología usada
Desarrollado sobre Django 4.1.2 + Python 3.10.6.
Utiliza una base de datos Sqlite. Incluye también DjangoRestFramework
para el desarrollo de las API's.

# Instalación en entorno local
~~~
$ git clone https://github.com/wilmays10/test-ego
$ cd test-ego
~~~
Ejecutar el script 'init_local.sh'
~~~
$ ./init_local.sh
~~~
# Consideraciones
El modelado de la base de datos contempla autómoviles para cualquier marca, modelo y versión.
De acuerdo al diseño entregado, tuve que considerar algunas versiones como modelos(por ejemplo:
la SW4 es una versión particular del modelo Hilux).

# Home
Una vez que esté ejecuntandosé el servidor local, se puede acceder al home:

http://localhost:8000/

# API's
Una vez que esté ejecuntandosé el servidor local, se puede acceder a las API's:

http://localhost:8000/api/

# Datos de administrador
Se proporciona datos de ejemplo que se cargaran al inicio. De todas formas, si quiere agregar a modificar datos se creo un usuario para esto:
- user: 'admin_ego'
- password: 'admin_ego'

El link de acceso para modificar datos:

http://localhost:8000/admin/