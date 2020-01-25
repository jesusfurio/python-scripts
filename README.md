# Python Scripts
Repositorio compuesto por script escritos en Python para sistemas operativos Linux.

## Pre-requisitos 📋
Es necesario tener instalado Python 3 en el equipo donde lo vayamos a utilizar. Si es necesario instalar algun paquete o librería adicional será detallado en la información del propio script.

### usb_boot
Requisitos:

* Tener instalado el paquete dd en el SO donde se vaya a ejecutar.

Script mediante el cual crearemos un usb booteable para instalar el sistema operativo que necesitemos en otro equipo. El funcionamiento es sencillo, una vez lo ejecutemos nos solicitará la ruta completa de donde se encuentre nuestro fichero .iso. Ejemplo:

```
/home/usuario/Descargas/ubuntu18.03.iso
```
A continuación el propio script nos mostrará las unidades disponibles donde queremos montar la ISO. Ej:

```
/dev/sdx
```

/!\ Cuidado con donde lo montas y asegurate de que es la unidad correcta.

### pokeapi
Requisitos:
* Instalar la librería requests en el SO o entorno virtual donde lo ejecutemos. Comando de instalación:
```
pip install requests
```
Pequeña aplicación que realiza consultas a la API Pokeapi y que nos devuelve los siguientes datos del Pokémon que introduzcamos en la llamada a la función "pokedex.load_pokemon":

* Nombre
* Tipo
* Habilidades
* URL con el sprite del Pokémon.

En un futuro este código se incluirá en una aplicación web para ver de manera más visual los datos devueltos por la API. Podeis ver con más detalle así como la documentación de Pokeapi a través de:

https://pokeapi.co/

### check_files
Requisitos:

* No es necesario instalar paquetes/librerías adicionales.

Este script en base a unas rutas absolutas que le indiquemos, los recorrera y borrará los ficheros que tengan fecha de creación mayor de X días.
La variable "folder" es una lista donde definiremos todas las rutas que queramos comprobar.
En la variable "delete_older_days" a partir de cuantos días de antigüedad borraremos los ficheros.

Este script es muy útil para servidores donde almacenemos backups y queramos borrar los antiguos.

### sql_files_backup
Requisitos:

* No es necesario instalar paquetes/librerías adicionales.

Con este script vamos a generar un dump de una base de datos MySQL y a la vez comprimiremos los ficheros ubicados en una ruta concreta. El nombre del fichero contendrá la fecha del día que se ha generado.
Una vez hecho, enviará el fichero comprimido generado al servidor que le indiquemos en función del valor de la variable "TYPE" (1 para FTP y 2 para SCP). Una vez hecho esto, borrará el fichero comprimido para no ocupar espacio en el servidor donde generemos la copia.

Es importante tener en cuenta que estamos utilizando variables de entorno con "os.environ.get" para almacenar usuarios, contraseñas, host de base de datos,etc. Estas variables de entorno deben ser definidas previamente en el fichero:

```
/etc/environment
```

## Construido con 🛠️
Librerías Python usadas:
* [Requests]: https://es.python-requests.org/es/latest/index.html - Realizar peticiones a una API.