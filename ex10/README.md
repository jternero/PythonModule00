
# Ejercicio de Animación de Carga

La función  `ft_bar(lst, timein)`  crea una barra de progreso animada en la consola mientras se itera sobre una lista. La barra de progreso muestra el porcentaje de elementos de la lista que se han procesado, así como el número de elementos procesados y el tiempo transcurrido desde el inicio del proceso. También se muestra una estimación del tiempo restante para completar el proceso.

## Uso

Para utilizar la función  `ft_bar(lst, timein)`, se deben proporcionar los siguientes argumentos:

-   `lst`: una lista que se debe iterar
-   `timein`: el tiempo de inicio del proceso

La función devuelve un iterador sobre la lista y muestra una barra de progreso animada en la consola.

Ejemplo de uso:

```
import time
from loading import ft_bar

my_list = range(3333)
ret = 0
timein = time.time()
for item in ft_bar(my_list, timein):
    ret += item 
    time.sleep(0.005)
print()
print(ret)

```

Este código muestra la barra de progreso animada mientras se itera sobre la lista  `my_list`. Al final, se muestra la suma de los elementos de la lista.
