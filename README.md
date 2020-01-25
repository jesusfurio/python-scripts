# Python Scripts
Repositorio compuesto por script escritos en Python para sistemas operativos Linux.

## Pre-requisitos
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