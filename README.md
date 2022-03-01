# Notas de Python

* Variables en minúsculas `my_variable = 1`

* Contantes en mayúsculas `MY_CONSTANTE = 1`

* Crear funciones se hace de la siguiente manera:

  ```python
  def function_name(arg1, arg2):
      return arg1 + arg2
  
  function_name(1,2)
  ```

  si la función no tiene un `return` regresa `None`, también se les puede conocer como métodos cuando se esta tratando con clases. Para asignar un valor por defecto a la función se hace de la siguiente manera:

  ```python
  def fuction_name(arg1, arg2=2):
      return arg1 + arg2
  
  function_name(1)
  ```

  métodos unidos a clases se llaman utilizando la notación punto:

  ```python
  import string
  
  print(string.ascii_lowercase)
  ```

* Los comentarios se ponen utilizando `#`.

* Los docstring son importantes para documentar el funcionamiento del código un ejemplo es el siguiente:

  ```python
  def power_of_two(n):
      """Eleva 2 a la potencia n
      
      :param n: int potencia
      :return: int - base 2 elevado a la potencia n
      
      Descripcion mas detallada de la funcion de ser necesario
      """
      return 2**n
  
  print(power_of_two.__doc__)
  ```

  

* El tipo `bool` puede ser `True` o `False`:

  * `False`
    * Constante es `None.`
    * Cero numérico de `int`, `float`, `complex`, `decimal` o `fraction`.
    * Colecciones o secuencias vacías `str`, `list`, `set`, `tuple`, `dict`, `range(0)`

  | Operador    | Operación                  | Descripción                                                  |
  | ----------- | -------------------------- | ------------------------------------------------------------ |
  | `and`       | "and boolean"              | Truth table of and gate                                      |
  | `or`        | "or boolean"               | Truth table of or gate                                       |
  | `not`       | "not boolean"              | Truth table of not gate                                      |
  | `>`         | "greater than"             | a > b  is True if a is **strictly** greater in value than b  |
  | `<`         | "less than"                | less than a < b is True if a is **strictly** less in value than b |
  | `==`        | "equal to"                 | equal to a == b is True if a is **strictly** equal to b in value |
  | `>=`        | "greater than or equal to" | greater than or equal to a >= b is True if a > b OR a == b in value |
  | `<=`        | "less than or equal to"    | less than or equal to a <= b is True if a < b or a == b in value |
  | `!=`        | "not equal to"             | not equal to a != b is True if a == b is False               |
  | `is`        | "identity"                 | identity a is b is True if and only if a and b are the same object |
  | `is not`    | "negated identity"         | negated identity a is not b is True if a and b are not the same object |
  | `in`        | "containment test"         | containment test a in b is True if a is member, subset, or element of b |
  | `not in`    | "negated containment test" | negated containment test a not in b is True if a is not a member, subset, or element of b |
  | `x < y < z` | "Comparison Chaining"      | an alternative to write less code in comparisons             |
  | `TypeError` | "Error message"            | error when implicit conversion does not work                 |

  * Algo muy importante con el operador `or ` se puede ver en el siguiente código:

    ```python
    def convert(number):
        text = str()
        if number % 3 == 0:
            text += 'Pling'
        if number % 5 == 0:
            text += 'Plang'
        if number % 7 == 0:
            text += 'Plong'
        return text or str(number)
        # if text is empty, bool is False then select str(number)
        # if it's not empty select the firt argument in the left
        
    print(convert(5))
    ```

    

* Hay tres tipos diferentes de números, enteros `int`, punto flotante `float`, y complejos `complex`. Fracciones `fractions.Fraction` y Decimales `decimal.Decimal` están disponibles importante la librería estándar.  Los números enteros , de clase`int` se pueden representar de las siguientes maneras: Hexadecimal `0x`, Octal `0o`, Binario `0b`.

* Para tener un `float` se puede utilizar la función para convertir, pero basta con poner un punto decimal al final del número para interpretar que es un `float`, ejemplo `a = 3.5`.

* Un número complejo se crea utilizando `j` o `J`, por ejemplo `a = 2.5 + 6.1j`. Para funcionalidades extra ver el módulo **cmath**.

* Operadores aritméticos:

  | Operador | Operación               |
  | -------- | ----------------------- |
  | `+`      | Suma                    |
  | `-`      | Resta                   |
  | `*`      | Multiplicación          |
  | `/`      | División                |
  | `//`     | Parte entera o truncado |
  | `%`      | Módulo o residuo        |

* Operador ternario:

  ```python
  x = 1 if a == 1 else 15
  ```

* Bloque de código `if`:

  ```python
  if x > y:
      print("x es mayor")
  ```

* Bloque de código `if - else`:

  ```python
  if x > y:
      print("x es mayor")
  else: 
      print("y es mayor")
  ```

* Bloque de código `if - elif - else`:

  ```python
  if x > y:
      print("x es mayor")
  elif x < y: 
      print("y es mayor")
  else:
      print("Son iguales")
  ```

* Los `str` son **secuencias inmutables**.

  * Se puede utilizar la estructura `for item in <str>` o `for index, item in enumerate(<str>)` para realizar operaciones de secuencias comunes.

  * Para acceder al primer elemento se utiliza el índice `0`

  * Y para acceder el último índice el `-1`

  * Los `str` se pueden concatenar con `+` o con `<str>.join(<iterable>)` y se pueden separar con `<str>.split(<separator>)`

  * Se pueden declarar `str` con `' ` o con `"`

  * Para `str` multilínea se utiliza `"""` o `'''`

  * Para convertir a `str` se puede utilizar la función `str()`

  * Las substring se pueden seleccionar utilizando **slice notation** `<str>[<start>:stop:<step>]` para producir otra string. Los resultados no incluyen el índice `stop`, siempre uno antes. Si no se da `start`, el índice de inicio es `0`. Si no se da `stop`, el índice final es el final del string.

  *  Por ejemplo consideremos las siguientes strings:

    ``moon_and_stars = '🌟🌟🌙🌟🌟⭐'``

    `sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'`

    | Ejemplo                | Resultado |
    | ---------------------- | --------- |
    | `moon_and_stars[1:4]`  | `'🌟🌙🌟'`   |
    | `moon_and_stars[:3]`   | `'🌟🌟🌙'`   |
    | `moon_and_stars[3:]`   | `'🌟🌟⭐'`   |
    | `moon_and_stars[:-1]`  | `'🌟🌟🌙🌟🌟'` |
    | `moon_and_stars[:-3]`  | `'🌟🌟🌙'`   |
    | `sun_and_moon[::2]`    | `'🌞🌞🌞🌞🌞'` |
    | `sun_and_moon[:-2:2]`  | `'🌞🌞🌞🌞'`  |
    | `sun_and_moon[1:-1:2]` | `'🌙🌙🌙🌙'`  |

  * Funciones con strings: para ver la lista completa acceder a [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)  

    | Función                                              | Descripción                                                  |
    | ---------------------------------------------------- | ------------------------------------------------------------ |
    | `<str>.split(<separator>)`                           | Regresa una lista de subtring dependiente del separador, default separador espacio |
    | `<str>.join(<iterable>)`                             | Regresa una string uniendo los elementos de una `list`, `tuple`, `set` o cualquier colección de entrada utilizando como unión `<str>` |
    | `<str>.startswith(<substr>)`                         |                                                              |
    | `<str>.endswith(<substr>)`                           |                                                              |
    | `<str>.title()`                                      | Cambia a mayúsculas el primer carácter de cada palabra que encuentre. |
    | `<str>.lower()`                                      |                                                              |
    | `<str>.upper()`                                      |                                                              |
    | `<str>.swapcase()`                                   |                                                              |
    | `<str>.isupper()`                                    |                                                              |
    | `<str>.islower()`                                    |                                                              |
    | `<str>.endswith(<suffix>)`                           | `True` si la string termina con `<suffix>`                   |
    | `<str>.strip(<char>)`                                | Devuelve la string pero con los caracteres `<char>` del principio y final removidos |
    | `<str>.lstrip(<chars>)`                              |                                                              |
    | `<str>.rstrip(<chars>)`                              |                                                              |
    | `<str>.replace(<substring>,<replacement substring>)` | Remplaza `<substring>` por `<replacement substring>`         |
    | `<str>.removeprefix(<substring>)`                    |                                                              |
    | `<str>.removesuffix(<substring>)`                    |                                                              |
    | `<str>.startswith`()                                 |                                                              |

  * Para trabajar con secuencias binarias se utilizan **binary sequence types** bajo **binary data service**, como `bytes`, `bytearray` y `memoryview`.

  * Las cadenas se comparan **lexicographically** y utiliza internamente la función `ord()`

  * Las **f-Strings** son la nueva manera para darle formato a una string desde python **3.6**  y se utilizan de la siguiente manera,

    ```python
    name = "Ciro"
    my_string = f"Hello {name}"
    print(my_string)
    ```

    

* Los **Exception messages** son mensajes necesarios que deben aparecer cuando se detecta una excepción. El mensaje debe ser significativo para poder indicar el origen del error. Cuando se conoce el origen y el tipo del error, uno puede elegir que aparezca el mensaje de error de uno de los tipos de [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes). Esto se hace con la sentencia `raise`.

  * Los errores que ocurren se conocen como `exception` y se requiere utilizar la sentencia `raise` en combinación.

  * Por ejemplo:

    ```python
    raise ValueError("Meaningful error message.")
    ```

* Las `list` son una colección de elementos en secuencia **mutable**. Son una estructura de dato extremadamente útiles.

  * Las listas pueden contener referencia a cualquier (o varios) tipos de datos, incluyendo otras listas o estructuras de datos como las `tuples`, `sets`, `dicts`.

  * Para iterar se pueden utilizar las siguientes estructuras:

    * `for item in <list>`
    * `for index, item in enumerate(<list>)`

  * El primer elemento de la lista se puede acceder con `<list>[0]` y el último con `<list>[-1]`

  * La **slice notation** es válida también en las listas.

  * Una lista se declara con `[]` y comas separando los elementos, o utilizando la función `list()`

    ```python
    empty_list = []
    one_element = ['Hola']
    two_element = ['Hola','perro']
    many_element = ['perro',123, 4.6]
    many_more_elements = [
        "rosas",
        "carmines",
        "pepinos"
    ]
    nested_list = [[1,2,3], [4,5,6]]
    ```

  * La función constructora `list()` solo acepta argumentos iterables.

    * Por ejemplo `a = list(6)` falla y salta un error
    * Por ejemplo `a = list( (16,) )` acepta a la tupla de un elemento y no salta ningún error

  * Las listas se pueden concatenar utilizando el operador `+`

    * Ejemplo `a = [1,2,3] + [4,5,6]` es igual a `a = [1,2,3,4,5,6]`

  * Se puede repetir la lista `n` veces si se utiliza el operador `*`

    * Ejemplo `a = [1,2,3] * 3` es igual a `a = [1,2,3,1,2,3,1,2,3]`

  * Es **IMPORTANTE** siempre utilizar la función `<str.copy()>` para hacer copias de las listas, a esto se le conoce como `shallow_copy`, de lo contrario modificar un elemento modificará los elementos de los otros porque la referencia es la misma.

  * **IMPORTANTE** manera de hacer una copia es utilizando slice notation, tal vez esta es la manera más sencilla.

  * Las listas son contenedores de **referencias**.

  * **IMPORTANTE** como las listas solo son contenedores, de variables, objetos o estructuras de datos anidadas, esas referencias de segundo nivel no son copiadas vía `shallow_copy` o slice. Modificar el objeto modificara todas las copias debido a que cada objeto lista solo contiene referencias apuntando a los contenedores de los elementos.

  * Un paquete importante para imprimir de forma estética las matrices o listas anidadas es:

    ```python
    from pprint import pprint
    ```

  * La manera correcta para crear una matriz llena de ceros es la siguiente:

    ```python
    from pprint import pprint
    
    # This is incorrect because the inner array is copy referencing itsef and changing one element will change the others
    game_grid = [[0]*8] *8
    
    # This loop will safely produce a game grid that is 8x8, pre-populated with zeros
    game_grid = []
    filled_row = [0] * 8
    for row in range(8):
        game_grid.append(filled_row.copy())
    
    pprint(game_grid)
    ```

  * Para un mejor manejo de listas es recomendable utilizar los paquetes [Numpy](https://numpy.org/) y [Pandas](https://pandas.pydata.org/) los cuales son mucho más robustos y eficientes.

  * Funciones con listas: para ver la lista completa visitar [`collentions.deque`](https://docs.python.org/3/library/collections.html#collections.deque)

    | Función                         | Descripción                                                  |
    | ------------------------------- | ------------------------------------------------------------ |
    | `<list>.copy()`                 | Hacer una copia de una lista, es necesario para evitar errores de direccionamientos de los objetos. |
    | `min(<list>)` / `max(<list>)`   | Calcula el mínimo valor de la lista / máximo valor de la lista |
    | `<list>.index(<value>)`         | Retorna el índice de la primera aparición de `<value>` en la lista, de lo contrario salta un error `ValueError`. si no se requiere el índice se puede utilizar el `in` el cual es más eficiente |
    | `<list>.appendleft()`           | Agrega un elemento al inicio de la lista                     |
    | `<list>.append()`               | Agrega un elemento al final de la lista                      |
    | `<list>.insert(<index>,<item>)` | Inserta un valor en el índice determinado                    |
    | `<list>.extend(<item>)`         | Para combinar una lista agregando `<item>` al final, internamente utiliza `<list>.append()` |
    | `<list>.reverse()`              | Hace un flip de la lista                                     |
    | `<list>.remove()`               | Remueve un elemento de la lista, lanza `ValueError` si no aparece en la lista |
    | `<list>.pop(<index>)`           | Remueve el elemento de índice `<index>` y lo retorna para su posterior uso, por defecto toma el último elemento |
    | `<list>.clear()`                | Remueve todos los elementos de la lista                      |
    | `<list>.sort()`                 | Utiliza [`Timsort`](https://en.wikipedia.org/wiki/Timsort) para ordenar la lista, por defecto los ordena de manera ascendente desde la izquierda |
    | `sorted(<iterable>)`            | Retorna una copia de la lista ordenada                       |
    | `<list>.count(<item>)`          | Retorna el número de veces que aparece el `<item>` en la lista |
    | `sum()`                         | Suma todos los elemento de la lista                          |
    | `len()`                         | Calcula el número de elementos de la lista                   |
    
  * Links para información adicional

    * [**Data Structures (Python 3 Documentation Tutorial)**](https://docs.python.org/3/tutorial/datastructures.html)
    * [**Lists and Tuples in Python (Real Python)**](https://realpython.com/python-lists-tuples/)
    * [**Python Lists (Google for Education)**](https://developers.google.com/edu/python/lists)

* Los **loops** son parte fundamental de la programación

  * `while`

  * `for`
    * Se utilizan mucho las funciones `range()` y `enumerate()`

  * Las sentencias `break` y `continue` se utilizan para controlar las iteraciones de los loops

  * También se puede utilizar la sentencia `else` para concluir cuando las iteraciones terminan. Las declaraciones que siguen a la palabra clave `else` no se ejecutaran si la ejecución termina con la sentencia `break`.

    ```python
    word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]
    
    # Using enumerate to get both an index and a value.
    
    for index, word in enumerate(word_list):
        print(index)
        word = word.title()
        if word.startswith("B"):
            print(f"{word} (at index {index}) starts with a B.")
            
    # This executes once *StopIteration* is raised and 
    # there are no more items to iterate through.
    # Note the indentation, which lines up with the for keyword.
    else:
        print(f"Found the above b-words, out of {len(word_list)} words in the word list.")
    ```

    

    ```python
    word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]
    for index, word in enumerate(word_list):
        word = word.title()
        if word.startswith("B"):
            print(f"{word} (at index {index}) starts with a B.")
        if word.startswith("S"):
            print("Found an S, stopping iteration.")
            break
    
    # This statement does not run, because a *break* was triggered.
    else:
        print(f"Found the above b-words, out of {len(word_list)} words in the word list.")
    ```

    

* Las `tuples` son colecciones de elementos en secuencia **inmutables**.

  * Para iterar se pueden utilizar las siguientes estructuras:
    * `for item in <tuple>`
    * `for index, item in enumerate(<tuple>)`
  * El primer elemento de la lista se puede acceder con `<tuple>[0]` y el último con `<tuple>[-1]`
  * La **slice notation** es válida también en las tuplas o se puede hacer una copia con `<tuple.copy()>`
  * Siendo inmutables no soportan las operaciones de secuencias mutables pero si las operaciones comunes de secuencias.
  * Las tuplas ocupan muy poco espacio en la memoria en comparación con otros tipos de colecciones y tienen un tiempo de acceso constante (O(1)) cuando se usa un índice. Sin embargo, no se pueden cambiar de tamaño, ordenar ni modificar una vez creados, por lo que son menos flexibles cuando se necesitan cambios o actualizaciones frecuentes en los datos. Si se requieren actualizaciones o expansiones frecuentes, una lista podría ser una mejor estructura de datos.
  * Una tupla se declara con `()` y comas separando los elementos, o utilizando la función `tuple()`
  * Para concatenar una tupla se puede utilizar el operador `+`
  * La tupla se puede convertir y regresar a tupla utilizando las funciones de `str()`,  `list()` y `tuple()`
  * El valor predeterminado de iteración para diccionarios es sobre las `keys`. Para incluir `keys` y `values` en una tupla creada a partir de un diccionario, hay que usar `<dict>.items()` que devolverá un iterador de tuplas `(key,value)`
  * Escribir los valores separados por coma cuenta como una tupla, pero es siempre recomendable utilizar los paréntesis para evitar confusiones 
  * Al igual que en las string y listas se puede utilizar el operador `in`
  * Las tuplas se utilizan a menudo como registros que contienen datos que son homogéneos desde el punto de vista organizativo o conceptual y se tratan como una sola unidad de información, incluso si los elementos individuales son de tipos de datos heterogéneos.
  * Las tuplas también se utilizan cuando se necesitan secuencias de datos homogéneas e inmutables para **hashability**, el almacenamiento en un `set` o la creación de `keys` en un diccionario.
  * Tenga en cuenta que, si bien las tuplas son inmutables en la mayoría de los casos, debido a que pueden contener cualquier estructura de datos u objeto, pueden volverse mutables si alguno de sus elementos es de un tipo mutable. El uso de un tipo de datos mutable dentro de una tupla hará que la tupla que la contiene  **unhashable**.






- Los `dict` es una estructura de dato de **tipo mapeo** que asocia por medio de un **hash** una `key` y un `value`. 


  - `keys` pueden ser `numbers`, `str`, `tuples`, o `frozensets`. 

  - `values` pueden ser cualquier tipo de dato o estructura, incluyendo otros diccionarios, tipos internos o personalizados, o incluso objetos como funciones o clases. 

  - Los diccionarios permiten extraer un `value` en un tiempo promedio constante, dada una `key`. 

  - Comparado con una `list`, los `dict` usan significativamente más espacio de memoria.

  - La búsqueda por medio de la llave es más eficiente que en una lista.

  - Los diccionarios son especialmente útiles en escenarios donde la colección de elementos es grande y es necesario acceder o actualizar los datos datos de manera frecuente.

  - Para crear un diccionario se puede utilizar la función `dict()`, la cual es un constructor de clase. o con declaración directa con la siguiente sintaxis: algo importante a tener en cuenta es que `keys` son tipo `str` y se usa `:` en lugar del signo igual.

    ```python
    bear = dict( name="Black Bear", speed=40, land_animal=True )
    whale = {"name": "Blue Whale", "speed": 35, "land_animal": False}
    ```

  - Para acceder a un valor del diccionario se hace `bear["speed"]` o  `bear.get("speed")`

  - Para cambiar valores se hace de la siguiente manera:

    ```python
    bear["name"] = "Grizzly Bear"
    whale["speed"] = 25
    ```

  - Para bucles en los diccionario podemos utilizar `for key in <dict>`

  - La mejor manera para trabajar diccionarios en bucles es:

    ```python
    for key,value in <dict>.items():
      	print(f'key: {key} \t value: {value}')
    ```

  - Funciones con diccionarios:

    | Función                            | Descripción                                        |
    | ---------------------------------- | -------------------------------------------------- |
    | `<dict>.keys()`                    |                                                    |
    | `<dict>.values()`                  |                                                    |
    | `<dict>.get(<key>,<default>)`      |                                                    |
    | `<dict>.pop(<key>)`                |                                                    |
    | `<dict>.setdefault(<key>,<value>)` | Argumento extra `default` si no encuentra la `key` |
    | `<dict.count()>`                   |                                                    |

    


- Un `set` es una colección de objetos **hashable** desordenados y **mutables**. Los elementos de un `set` son únicos y no se permiten los duplicados.

  - Los `sets` pueden almacenar cualquier tipo de tipos de datos siempre y cuando esos tipos  puedan ser hash.

  - Los sets también pueden ser **inmutables** si son `frozenset`.

  - Los `set` soportan el operador `in`, `len()`, `copy()`

  - Para iterar los sets se utilizan la sintaxis `for item in <set>`

  - A diferencia de los tipos de secuencias (`string`,`list` y `tuple`), los `sets` no están ordenados ni indexados, y no admiten el corte, la clasificación u otros comportamientos de tipo secuencia.

  - Los sets se utilizan más comúnmente para deduplicar rápidamente grupos de elementos.

  - También se utilizan para realizar pruebas rápidas de pertenencia, encontrar superconjuntos y subconjuntos de elementos y realizar "matemáticas de conjunto" (cálculo de unión, intersección, diferencia y diferencia simétrica entre grupos de elementos).

  - Los conjuntos ahorran más espacio que un diccionario de solo `keys` y son más rápidos que una lista o una matriz para la pertenencia, a menos que necesite realizar un seguimiento de los elementos secuenciados o duplicados.

  - Los `set` pueden ser declarados con `{}` y sus elementos separados por comas.

  - Para declarar un `set` y no confundirse con diccionarios se utiliza la función constructora `set()` 

  - Los elementos repetidos no se agregan como elemento del set.

  - Funciones con `sets`

    | Función                                                      | Descripción                                                  |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | `<set>.issubset(<other_collection>)` / `<set> <= <other_set>` | Subconjunto                                                  |
    | `<set>.issuperset(<other_collection>)` / `<set> >= <other_set>` | Superconjunto                                                |
    | `<set>.isdisjoint(<other_collection>)`                       | Disjunto, verdadero si no tienen elementos en común          |
    | `<set>.union(*<other iterables>)` y `<set> |<other set 1> |<other set 2> |... |<other set n>` | Unión de conjuntos                                           |
    | `<set>.difference(*<other iterables>)` y `<set> - <other set 1> - <other set 2> - ...<other set n>` | Diferencia de conjuntos                                      |
    | `<set>.intersection(*<other iterables>)` y `<set> & <other set> & <other set 2> & ... <other set n>` | Intersección de conjuntos                                    |
    | `<set>.symmetric_difference(<other iterable>)` y `<set> ^ <other set>` | Diferencia simétrica, retorna un set que contiene los elementos que están en `set` o en `other` pero no en los dos |

  - Aqui agregar cosas extra


​     



## Lista de funciones generales


| Función                 | Descripción                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `dir()`                 | **IMPORTATANTE** Ver todos los métodos e información de una clase `dir(x)` donde `x = [1,2,3]` |
| `help()`                | **IMPORTANTE** Ver la documentación de una función o método por ejemplo `help(x.sort)` |
| `function_name.__doc__` | **IMPORTANTE** Mostrar documentación de función o clase.     |
| `exit()`                | Salir de la terminal de python                               |
| `print()`               | Imprimir                                                     |
| `type()`                | Tipo de dato o clase                                         |
| `len()`                 | Tamaño de colecciones o secuencias                           |
| `bool()`                | Convertir a booleano                                         |
| `int()`                 | Convertir a entero                                           |
| `hex()`                 | Convertir a representación en hexadecimal                    |
| `oct()`                 | Convertir a representación en octagonal                      |
| `bin()`                 | Convertir a representación en binaria                        |
| `float()`               | Convertir a punto flotante                                   |
| `complex()`             | Doc argumentos, crear un número complejo                     |
| `str()`                 | Convertir a tipo `str`                                       |
| `ord()`                 | Valor en ascii, se utiliza internamente al comparar `str`    |
| `id()`                  | Para ver el identidad de un objeto. El identificador de un objeto nunca cambia después de su creación, intensamente se utiliza al utilizar los comparadores `is` y `is not` |
| `list()`                | Crear un objeto lista de la entrada                          |
| `range()`               | Crea una secuencia de enteros, muy utilizado en ciclos for   |
| `round()`               | Redondear                                                    |
| `all()`                 | Retorna `True` si todos los elementos de la variable iterable son `True` |



## Comprehension list

Lo mejor es dar algunos ejemplos para entender su funcionamiento:

```python
# Crear una lista del 0 al 99
x = [i for i in range(100)]

# Crear una lista del 1 al 99 de 2 en 2
x = [i for i in range(1,100,2)]

# Crear una lista del 0 al 98 si es un número par
x = [i for i in range(100) if i % 2 == 0]

# Crear una lista del 0 al 98 si es un número par
x = [i for i in range(0,100,2)]

# Crear una lista de los valores de x que son diferentes a los de y
x = 'pepe'
y = 'papo'
z = [i for i,j in zip(x,y) if i != j]

```



* Las clases son definiciones combinando información (conocida como `attributes`, `properties`, `data members`, `variables`,  o `fields`)  con `functions`(también conocidos como `methods`). Las definiciones de clases son utilizadas para crear copias o `instances` de una clase, comúnmente conocidos como `objects`. Los objetos pueden representar entidades del mundo real (como carros o gatos) o conceptos más abstractos (como vehículos o mamífero). Cada objeto es único en la memoria de la computadora y representa una parte de un modelo general. Las clases y los objetos se pueden encontrar en varios paradigmas de programación, pero son una parte integral de la OOP (Object Oriented Programming), en el que los programas están formados por objetos que interactúan entre sí.

  * Las clases son las definiciones de nuevos tipos de objeto, y por las cuales nuevas `instances` de objetos son creadas. A menudo agrupan datos con código o funciones que operan con esos datos. En este sentido, las clases son planos o conjuntos de instrucciones a partir de los cuales se pueden construir y utilizar muchos objetos de un tipo similar. Un programa complejo puede tener muchas clases, cada una de las cuales crea muchos sabores diferentes de objetos. El proceso de construir un objeto a partir de una clase se conoce como instanciación (o creación de una instancia de la clase).

  * Una definición de clase en Python es sencilla:

    ```python
    class MyClass:
        # Class body goes here
    ```

  * Los campos de la clase (también conocidas como `properties`, `attributes`, `data members`, o `variables`) pueden añadirse al cuerpo de la clase:

    ```python
    class MyClass:
        number = 5
        string = "Hello!"
    ```

  * Una instancia (objeto) de `MyClass` se puede crear o unir a un nombre llamando a la clase, de la misma manera en la que se llama a una función:

    ```python
    new_object = MyClass()
    ```

  * `Class attributes` son compartidos por todos los objetos (o instancias ) creadas por una clase, y pueden accederse vía `dot notation` aka un `.` colocado después del nombre del objeto y antes del nombre del atributo.

    ```python
    new_object = MyClass()
    new_object.string
    ```

  * Los atributos de clase se definen en el cuerpo de la clase misma, antes que cualquier otro método. Son propiedad de la clase, lo que les permite compartirse entre instancias de la clase. Debido a que estos atributos son compartidos, se puede acceder a su valor y manipularlo directamente desde la clase. La alteración del valor de los atributos de clase altera el valor de **todos los objetos instanciados desde la clase**:

    ```python
    obj_one = MyClass()
    obj_two = MyClass()
    obj_two.number
    MyClass.number
    MyClass.number = 27
    obj_one.number
    obj_two.number
    ```

  * Tener un montón de objetos con datos sincronizados en todo momento no es particularmente útil. Afortunadamente, los objetos creados a partir de una clase se pueden personalizar con sus propios `instance attributes` (o instance properties, variables, or fields). Como sugiere su nombre, los atributos de instancia son únicos para cada objeto y se pueden modificar de forma independiente.

  * El [dunder method](https://www.dataindependent.com/python/python-glossary/python-dunder/) (short for double underscore method) `__init__()` es usado para personalizar las instancias de la clase, y puede utilizarse para inicializar los atributos o propiedades de una instancia. Por su papel en la inicialización de atributos de instancia, `__init__()` también se conoce como constructor o inicializador de clase. `__init__()` toma un parámetro requerido llamado `self`, que se refiere al objeto recién inicializado o creado. Los datos de atributos o propiedades de instancia se pueden pasar como argumentos de `__init__()`, siguiendo el parámetro `self`.

  * A continuación, `MyClass` ahora tiene atributos de instancia llamados `location_x` y `location_y`. Como puede ver, los dos atributos se han asignado al primer y segundo índice del argumento de `location` (una tupla) que se ha pasado a `__init__()`. Los atributos `location_x` y `location_y` para una instancia de clase ahora se inicializarán cuando cree una instancia de la clase y se cree un objeto:

     ```python
     class MyClass:
         number = 5
         string = "Hello!"
         
         def __init__(self, location):
             self.location_x = location[0]
             self.location_y = location[1]
             
     new_object_one = MyClass((1, 2))
     new_object_two = MyClass((-8, -9))
     new_object_one.location_x
     new_object_two.location_x
     ```

  * Tenga en cuenta que solo necesita pasar un argumento al inicializar `MyClass` arriba: Python se encarga de pasarse `self` cuando se llama a la clase.

  * Un `method` es una función que está vinculada a la clase misma (conocido como [class method](https://stackoverflow.com/questions/17134653/difference-between-class-and-instance-methods), que se analizará en un ejercicio posterior) o a una instancia de la clase (objeto). Los métodos que operan en un objeto (instancia) deben definirse con `self` como primer parámetro. A continuación, puede definir el resto de los parámetros como lo haría para una función "normal" o no vinculada.

  * Al igual que el acceso a los atributos, llamar a un método simplemente requiere colocar un `.` después del nombre del objeto y antes del nombre del método. El método llamado no necesita una copia del objeto como primer parámetro. Python completa `self` automáticamente.

  * Se puede acceder a los atributos de clase desde dentro de los métodos de instancia de la misma manera que se accede fuera de la clase.

  * La palabra clave `pass` es un marcador de posición sintácticamente válido: evita que Python arroje un error de sintaxis o un error` NotImplemented` para una función o definición de clase vacía. Esencialmente, es una forma de decirle al intérprete de Python: ¡No te preocupes! Eventualmente pondré el código aquí, solo que aún no lo he hecho.

    ```python
    class MyClass:
        number = 5
        string = "Hello!"
    
        def __init__(self, location):
            self.location_x = location[0]
            self.location_y = location[1]
    
        def change_location(self, amount):
            self.location_x += amount
            self.location_y += amount
            return self.location_x, self.location_y
    
        def increment_number(self):
            MyClass.number += 1
            
    	def pending_functionality(self):
           pass
    
    test_object = MyClass((3,7))
    (test_object.location_x, test_object.location_y)
    test_object.change_location(7)
    
    test_object_one = MyClass((0,0))
    test_object_one.number
    test_object_two = MyClass((13, -3))
    test_object_two.increment_number()
    test_object_one.number
    ```

  * asd

  







## OOP Object Oriented Programming

**Object-oriented programming** (OOP) is a method of structuring a program by bundling related properties and behaviors into individual **objects**. 

Object-oriented programming is a [programming paradigm](http://en.wikipedia.org/wiki/Programming_paradigm) that provides a means of structuring programs so that properties and behaviors are bundled into individual **objects**.

For instance, an object could represent a person with **properties** like a name, age, and address and **behaviors** such as walking, talking, breathing, and running. Or it could represent an [email](https://realpython.com/python-send-email/) with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.







## Imprimir la lista de todos los métodos de una clase

```python
method_list = [method for method in dir(MyClass) if method.startswith('__') is False]
print(method_list)

method_list = [attribute for attribute in dir(MyClass) if callable(getattr(MyClass, attribute)) and attribute.startswith('__') is False]
print(method_list)

```



## PIP

| Comando                      | Descripción         |
| ---------------------------- | ------------------- |
| `pip install <package_name>` | instalar un paquete |



## Project Euler

Problemas verdaderamente difíciles 

https://projecteuler.net/register



## PEPs

Significa [Python Enhancement Proposals](https://www.python.org/dev/peps/), y es una documentación que sirve como guía para escribir de manera correcta y estandarizada, códigos, documentaciones entre otras cosas en Python.

Por ejemplo una de las más importantes es la [PEP8](https://www.python.org/dev/peps/pep-0008/) la cual lleva como título **Style Guide for Python Code**, algunas reglas dentro de esta PEP son las siguientes:

* Usar 4 espacios por nivel de identación.
* Limitar las líneas a un máximo de 79 caracteres.
* Al importar paquetes estos generalmente deben estar en líneas separadas.
* Los paquetes importados siempre se colocan en la parte superior del archivo, justo después de los comentarios y cadenas de documentación del módulo, y antes de las constantes y globales del módulo.
* Aunque no sea necesario, poner paréntesis cuando se crean tuplas. Por defecto no son necesarias pero es buena practica ponerlos. 