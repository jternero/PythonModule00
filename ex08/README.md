
# Ejercicio de Cifrado

El objetivo de este ejercicio es crear un programa que convierta un mensaje de texto en código Morse.

El diccionario  `MORSE_CODE_DICT`  contiene la traducción de cada letra, número y caracter especial del alfabeto al código Morse.

La función  `encrypt(message)`  toma como argumento un mensaje en texto plano y devuelve una cadena de texto con el mensaje convertido en código Morse.

La función  `encrypt()`  itera sobre cada letra del mensaje y busca su correspondiente en el diccionario  `MORSE_CODE_DICT`. Si la letra no se encuentra en el diccionario, se devuelve un mensaje de error.

## Cómo utilizar el programa

Para utilizar el programa, se debe correr el archivo  `MorseCode.py`  en la línea de comandos, con un argumento:

-   `message`: un string que representa el mensaje que se desea cifrar.

Por ejemplo:

```
python3 MorseCode.py "Hola, este es un mensaje en código Morse"

```

El programa mostrará el mensaje cifrado en código Morse.

## Errores

El programa muestra un mensaje de error en el siguiente caso:

-   Si la letra a cifrar no se encuentra en el diccionario  `MORSE_CODE_DICT`.
