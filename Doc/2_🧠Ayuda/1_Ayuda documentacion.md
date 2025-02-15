<div style="text-align: justify;">

# ✏️ Ayuda Documentación

Esta documentación ha sido creada por javierperez@uma.es para alojar toda la información sobre la asignatura "Diseño y Desarrollo de un Sistema Mecánico" del curso 2024/25, compilado usando Sphinx y la plantilla de Read the Docs. El objetivo principal es la generación de documentación por parte de todos los miembros sin necesidad de escribir código (No-code / Zero-code). Para ello, se hace uso de una estructura de carpetas y archivos .md/.rst publicados en el repositorio de GitHub.

## 1. Compilación de Documentación

Con el fin de convertir los ficheros (.md y .rst) en una web "Read the Docs" es necesario compilar el texto a .html. Esto se logra gracias a Sphinx, que es un compilador de documentación para Python.

### 1.1 Compilación Local (Difícil)

Para la compilación local es necesario tener instalado Python 3 y las siguientes librerías: `pip install sphinx_rtd_theme recommonmark sphinx-autobuild myst-parser sphinxemoji linkify-it-py`. La compilación se realiza utilizando el comando `sphinx-build Documentacion Documentacion/_web` en la línea de comandos desde la carpeta de Documentacion.

### 1.2 Compilación en GitHub (Fácil)

La compilación en GitHub, por el contrario, no requiere instalar Python. Simplemente al subir los archivos a GitHub utilizando "Bash", "MatLab" o "GitHub Desktop" (Recomendado), se lanza una acción en nuestro servidor web en menos de un minuto automáticamente la documentación que compila. En este caso, tener acceso a la documentación compilada es tan fácil como realizar un "commit/push" y esperar 1 minuto.

## 2. Archivos Compatibles

### 2.1 Archivos .md (No-code)

Estos archivos permiten redactar la documentación sin preocuparse del código. Pueden ser editados por el programa MarkText (software libre), similar a la edición de un archivo Word. Este formato es muy limitado y estructurado para aportar facilidad a la hora de comprender la documentación generada. Para mejorar la presentación en la web, el texto se justifica automáticamente al lanzar la compilación. Las imágenes centradas se mantienen así gracias a una modificación del .md realizada automáticamente.  [Enlace emojis](https://emojidb.org/)

### 2.2. Archivos .rst (Low-code)

Si el archivo .md os parece muy limitado y queréis hacer algo más "interesante", podéis utilizar un archivo .rst, aunque no aporta mucho teniendo en cuenta que se pierde la visualización directa del texto sin compilar. Sphinx está pensado originalmente para utilizar este tipo de fichero, pero es necesario escribir código para su utilización. En esta ayuda hay un apartado de ejemplo por si a alguien le apetece hacerlo de esta forma.

</div>
