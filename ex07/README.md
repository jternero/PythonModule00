
# Ejercicio de Manipulación de Cadenas

El objetivo de este ejercicio es crear un programa que filtre palabras de una cadena de texto y muestre aquellas palabras que tienen una longitud mayor a un número determinado.

La función  `filterwords(s, n)`  toma dos argumentos:

-   `s`: un string que representa el texto a filtrar.
-   `n`: un entero que representa la longitud mínima de las palabras que se van a mostrar.

La función  `filterwords()`  divide el texto en palabras y crea una lista con las palabras que tienen una longitud mayor a  `n`. Si no hay palabras que cumplan con estas condiciones, se muestra un mensaje indicando que no hay palabras bajo esa condición.

## Cómo utilizar el programa

Para utilizar el programa, se debe correr el archivo  `FilterWords.py`  en la línea de comandos, con dos argumentos:

-   `s`: un string que representa el texto a filtrar.
-   `n`: un entero que representa la longitud mínima de las palabras que se van a mostrar.

Por ejemplo:



```
python3 FilterWords.py "Hola, este es un ejemplo de texto para filtrar palabras" 4

```

El programa mostrará todas las palabras del texto que tienen una longitud mayor a 4.

## Errores

El programa muestra un mensaje de error en los siguientes casos:

-   Si no se proporcionan argumentos al programa.
-   Si se proporcionan más de dos argumentos al programa.
-   Si el segundo argumento no es un número entero.
