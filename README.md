# Repositorio de Programación Orientada a Objetos con Python

Repositorio con ejercicios de Programación Orientada a Objetos

## 1. Crear -gitignore

Crear el archivo .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el repositorio

````shell
* .pyc
_pycache_/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos no deseados que se guardan en el repositorio

````shell
git add .
````

## 3. Crear un COMMIT 

Crea un commit o punto de control de los cambios realizados en el proyecto

````shell
git commit -m "CREATED .gitignore"
````

* CREATED - Se crearon nuevas carpetas o archivos.
* UPDATED - Se actualizaron o agregaron nuevas funciones.
* FIXED - Se corrigieron funciones.

## 4. Realizar el COMMIT.

````shell
git push -u origin main
````

## 5. Realizar documentación 

Agregar un Docs String a lor metodos generados.

````python
(""") - Indica los parametros y que hace con ellos.
(Args) - Define las variables de entrada. 
(Return) - Define las variables resultantes de los procesos (metodos) que se dvuelven.
(""") - Fin y cierre de los comentarios.
````
