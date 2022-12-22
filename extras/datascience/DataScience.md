# Data Science - Manual numpy, matplotlib, pandas 

## 1. Introducción

* Lo primero que hay que tener presente es que es necesario conocer los fundamentos básicos de python, listas, tuplas, diccionarios, set, loops, tipos de datos, funciones de conversión y de tipo y como funcionan las clases. Esto es necesario ya que al utilizar paquetes en python el operador punto `.` tanto para acceder a métodos de la clase como a atributos.

### 1.1 Instalación

* Para trabajar en cualquier proyecto nuevo se recomienda crear un entorno virtual para contener todas los paquetes necesarios así como las versiones de estos. Además es recomendable siempre crear una carpeta nueva por cada proyecto. Dentro de esta crear el entorno virtual con el nombre de `venv`, de modo que de ser necesario podemos eliminar y generar nuevamente el entorno sin perder información.
* Seguir los siguientes pasos para comenzar a trabajar:

1. Crear una carpeta con el nombre del proyecto y dentro de esta otra carpeta llamada `codigos`.

2. Crear un entorno virtual dentro de la carpeta del proyecto con el siguiente comando:

   ```
   python -m venv venv
   ```

3. Activar el entorno virtual con el comando estando dentro de la carpeta del proyecto:

   ```
   venv/Scripts/activate.bat
   ```

4. Actualizar pip:

   ```
   python -m pip install --upgrade pip
   ```

5. Instalar los paquetes :

   ````
   numpy
   matplotlib
   pandas
   jupyterlab
   ````

6. Para salir del entorno virtual utilizar el comando:

   ```
   deactivate
   ```

7. Abrir jupyterlab con el comando:

   ```
   jupyter lab
   ```

* Es preferible trabajar con jupyterlab en lugar de jupyter notebooks ya que el primero es la evolución del segundo y es para donde se esta dirigiendo la comunidad, además de que es mejor al momento de leer archivos csv y tener graficas interactivas.



### 1.2 Utilización de jupyterlab



#### Atajos

| Atajo           | Descripción                                    |
| --------------- | ---------------------------------------------- |
| `Ctrl + Enter`  | Ejecutar celda actual                          |
| `Shift + Enter` | Ejecutar celda actual y moverse a la siguiente |
| `Alt + Enter`   | Ejecutar celda actual e insertar celda abajo   |
| `Ctrl + s`      | Guardar                                        |
| `a`             | Insertar una celda arriba                      |
| `b`             | Insertar una celda abajo                       |
| `x`             | Cortar celda                                   |
| `c`             | Copiar celda                                   |
| `v`             | Pegar celda                                    |
| `Shift + V`     | Pegar celda arriba                             |
| `dd`            | Borrar celda                                   |
| `z`             | Deshacer                                       |
| `y`             | Cambiar celda a tipo **Code**                  |
| `m`             | Cambiar celda a tipo **Markdown**              |





