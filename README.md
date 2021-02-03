# Scripts-TFG

Scripts creados para la utilización y la introducción periódica en la base de datos del proyecto [Sonidos del Cielo](http://sonidosdelcielo.org/)

## Instalación de Python

Antes de nada es necesario tener instalado el lenguaje `Python`

> Instalación en Windows

- Es necesario descargar la versión indicada para la versión del sistema operativo (32 o 64 bits), esto se puede hacer desde la siguiente [web](https://www.python.org/downloads/windows/).

- Pincha en el enlace ``Latest Python 3 Release -Python x.x.x``. Si el ordenador utiliza la versión de 64 bits, descarga ***Windows x86-64 executable installer***, de lo contrario, descarga ***Windows x86 executable installer***.

- Ejecutar el instalador y asegurarse de marcar la casilla ``Add Python to PATH``.

> Instalación en macOS

- Es necesario visitar la siguiente [página](https://www.python.org/downloads/release/python-361/) y descargar el instalador de Python.
- Hacer doble click sobre el pkg descargado y ejecutar el instalador.

## Prerrequisitos

Para instalar las dependencias neceasrias, ejecutar el comando ``pip3 install -r requirements.txt``.

## Utilización

- Primero, es necesario cambiar en el código la dirección dónde se encuentra el fichero CSV con las detecciones. 

- Posteriormente, abrir un terminal y correr el fichero mediante el comando `python3 run main.py`.

- Automáticamente se añadirán los ecos, las curvas de luz, los espectrogramas y los nuevos sonidos a la base de datos.
