# Ejercicio de Juego de Adivinanza

El objetivo de este ejercicio es crear un programa que permita al usuario adivinar un número secreto generado al azar.

La función  `guess_number()`  es la función principal que ejecuta el juego. El número secreto se genera al azar utilizando la función  `random.randint(1, 99)`. El juego comienza con un mensaje de bienvenida y luego entra en un ciclo  `while`  que pide al usuario que adivine el número secreto. Si el usuario ingresa la palabra "exit", el juego termina. Si el usuario ingresa un número fuera del rango de 1 a 99, el programa le indica que el número está fuera de rango y le pide que ingrese otro número. Si el usuario ingresa un número dentro del rango, el juego le indica si el número es demasiado bajo o demasiado alto. Si el usuario adivina el número secreto, el programa le indica cuántos intentos le tomó adivinar el número.

El programa también tiene un mensaje de error que se muestra si se ingresan demasiados argumentos en la línea de comandos.

## Cómo utilizar el programa

Para utilizar el programa, se debe correr el archivo  `GuessNumber.py`  en la línea de comandos. No se necesitan argumentos adicionales.

Por ejemplo:

```
python3 GuessNumber.py
```

El programa mostrará el mensaje de bienvenida y pedirá al usuario que adivine el número secreto. Si el usuario adivina el número, el programa le indicará cuántos intentos le tomó adivinar el número.

## Errores

El programa muestra un mensaje de error en el siguiente caso:

-   Si se ingresan demasiados argumentos en la línea de comandos.
