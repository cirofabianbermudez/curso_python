# Manual de numpy

 ¿Por que utilizar numpy en lugar de listas?. Porque numpy es más rápido que utilizar listas. numpy utiliza Fixed Type, por ejemplo int32 y se puede especificar el tamaño que queremos que utilice. Las listas almacenan más información porque guardan Size, Reference Count, Object Type y Object Value. numpy utiliza memoria continua mientas que las listas no. numpy no necesita hacer comprobaciones para cada uno de sus elemento debido a que todos los elemento en un arreglo numpy tienen el mismo tipo. Los arreglos en numpy tienen los mismos métodos que las listas normales y muchos otros más.
Por lo anterior numpy es un remplazo para MATLAB, la instalación de python toma menos de 10 min y configurar un entorno también, mientras que la instalación de MATLAB toma entre 1 y 2 horas. En combinación con Matplotlib es una herramieta muy buena para realizar gráfica. Es el backend para otros paquetes como Pandas y es la base para realizar algoritmos de Machine Learnig.

## 1. Introducción (uso básico)

Lo primero que hay que hacer es importa la libreria de numpy, tradicionalmente se hace de la siguiente manera:


```python
import numpy as np
```

Para declarar un arreglo sencillo en numpy o un vector 1D lo hacemos de la siguiente manera:


```python
a = np.array([1,3,5])
print(a); print(type(a)); print(a.ndim); print(a.shape); print(a.dtype); print(a.itemsize); print(a.size); print(a.nbytes)
#print(dir(a))
```

    [1 3 5]
    <class 'numpy.ndarray'>
    1
    (3,)
    int32
    4
    3
    12
    




    <function ndarray.sum>



como podemos notar, se utiliza el método `np.array()` el cual toma como argumento una lista de python.

Para crear una matriz 2x2 lo podemos hacer pasando una lista de listas de la siguiente manera:


```python
b = np.array( [ [1.1,2.2,3.3],[4.4,5.5,6.6] ] )
print(b); print(type(b)); print(b.ndim); print(b.shape); print(b.dtype); print(a.itemsize); print(a.size); print(a.nbytes)
#print(dir(b))
```

## 2. Arreglos

Ya vimos como crear arreglos apartir de listas, sin embardo numpy tiene maneras más eficientes de crear arreglos, acontinuación se muestran algunas de las más importantes:

| Tipo básico | Código |
| --- | --- |
| Matriz | `a = np.array( [ [1,2], [3,4] ] )` |
| Escalar | `b = np.array( [ [1] ] )` |
| Vector renglón | `c = np.array( [ [1,2,3,4]] )` |
| Vector columna | `d = np.array( [ [1],[2],[3],[4] ] )` |



```python
a = np.array( [ [1,2], [3,4] ] ); print(a); print(a.shape); print('')
b = np.array( [ [1] ] ); print(b); print(b.shape); print('')
c = np.array( [ [1,2,3,4]] ); print(c); print(c.shape); print('')
d = np.array( [ [1],[2],[3],[4] ] ); print(d); print(d.shape); print('')
```

    [[1 2]
     [3 4]]
    (2, 2)
    
    [[1]]
    (1, 1)
    
    [[1 2 3 4]]
    (1, 4)
    
    [[1]
     [2]
     [3]
     [4]]
    (4, 1)
    
    

### Funciones para crear arreglos

| Comando | Descripción |
| --- | --- |
| |  |
| | |
| | |
| | |

## 3. Indexación

La indexación es la forma de extraer y modificar los valores de los arreglos. La posición de un valor dentro de un arreglo es su índice. El índice se puede utilizar para extraer valores concretos.

Supongamos un vector de la forma `x = np.arange(1,11) `, entonces podemos realizar las siguientes indexaciones:


```python

```
