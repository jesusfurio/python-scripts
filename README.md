# Python Scripts
Repositorio compuesto por script escritos en Python para sistemas operativos Linux.

## Pre-requisitos
Es necesario tener instalado Python 3 en el equipo donde lo vayamos a utilizar. Si es necesario instalar algun paquete o librería adicional será detallado en la información del propio script.

### usb_boot
Script mediante el cual crearemos un usb booteable para instalar el sistema operativo que necesitemos en otro equipo. El funcionamiento es sencillo, una vez lo ejecutemos nos solicitará la ruta completa de donde se encuentre nuestro fichero .iso. Ejemplo:

```
/home/usuario/Descargas/ubuntu18.03.iso
```
A continuación el propio script nos mostrará las unidades disponibles donde queremos montar la ISO. Ej:

```
/dev/sdx
```

/!\ Cuidado con donde lo montas y asegurate de que es la unidad correcta.

