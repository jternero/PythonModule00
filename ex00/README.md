
# Instalación y creación del entorno Python

Este script automatiza la instalación de conda y la creación de un entorno Python para este curso.

## Pasos

1.  Descarga el script  `install_python_env.sh`
2.  Dale permisos de ejecución con  `chmod +x install_python_env.sh`
3.  Ejecútalo con  `. ./install_python_env.sh`
4.  Sigue las instrucciones en la terminal.

El script:

-   Detecta automáticamente si tienes MacOS o Linux
-   Descarga e instala el instalador de conda
-   Instala conda en un path personalizado  `/goinfre/$USER/miniconda3`
-   Inicializa conda para tu shell (.bashrc o .zshrc)
-   Crea un entorno llamado  `42AI-$USER`  con Python 3.7 y los paquetes requeridos
-   Muestra los comandos para activar el entorno

## Comprobar la instalación

-   `conda info --envs`: Muestra los entornos disponibles
-   `conda activate 42AI-$USER`: Activa el entorno
-   `which python`: Muestra la ruta del intérprete de Python activo
-   `python -V`: Muestra la versión de Python
-   `python -c "print('Hello World!')"`: Ejecuta un pequeño script Python

Si tienes problemas, repite los pasos 1 a 3. Ten en cuenta que debes volver a actualizar  
tu archivo  `.bashrc`  o  `.zshrc`  después de una nueva ejecución del script.
