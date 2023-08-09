# Sistema de Reportes Siglo

### Planteamiento del problema

La aplicación tiene como objetivo agilizar la creación de informes de ventas para cada proveedor de nuestra empresa. Esto reemplaza el proceso anterior que solía ser manual y que implicaba dar formato y estilo a los informes en Excel. Además, esta aplicación mejora significativamente la apariencia visual de los archivos PDF generados. 


### Descripcion del sistema

El sistema aborda la problemática previamente planteada al recibir como punto de partida un archivo DBF que contiene los datos de ventas de libros por cada proveedor. Estos datos se agrupan en base al número de corte asignado en el archivo anterior, lo que da como resultado una estructura de datos que incluye a cada proveedor junto con sus registros respectivos.

En esta etapa, se llevan a cabo operaciones para calcular el total bruto y neto. Se realizan cálculos matemáticos en cada registro de cada proveedor. Además, se seleccionan los campos necesarios de cada registro para su inclusión en los informes.

Con la lista de proveedores y sus registros, se realiza un recorrido para generar y agregar los informes a una nueva lista de archivos. Esta lista permitira crear un archivo zip para retornar todos los reportes generados para cada proveedor.

Para calcular el total por cada proveedor, se recorren los registros correspondientes y se suman en una variable acumuladora. Este proceso permite obtener los totales de todos los registros de libros para cada proveedor. De manera similar, se realiza un proceso análogo para calcular el total de libros devueltos.

### Tecnologias utilizadas para la construccion del sistema

- [Python] - lectura de archivos, procesos matematicos y lenguaje base
- [Django] - framework, servidor y vistas
- [Pillow] - libreria para el manejo de imagenes
- [Tailwind] - framework css
- [Js] - lenguaje de programacion para interactividad
- [Openpyxl] - libreria para el maneko de archivos excel
- [Weasyprint] - libreria para la creacion de archivos pdf
- [Dbfread]- libreria para manipular archivos dbf
- [Git]- control de versiones


[Repositorio del aplicacion](https://github.com/SantiBj/Reports-.git)


## Requerimientos 

 [Python](https://www.python.org/downloads/) v3.10+ .

Los siguientes pasos se deben ejecutar desde la terminal de comandos situandonos en la carpeta del proyecto:

Instalacion de virtualenv
```sh
pip install virtualenv
```

Creacion del entorno virtual 
 ```sh
virtualenv env
```

Activacion del entorno virtual
```sh
source env/bin/activate
```
Instalacion de las dependencias del proyecto
```sh
pip install -r requirements.txt
```

### Como poner en marcha el sistema en linux

- Iniciar el entorno virtual para que el sistema puedo utilizar todas la dependencias que requiere
    ```sh
    source env/bin/activate
    ```
- Ejecutar el comando para poner en marcha el servidor 
     ```sh
    python3 manage.py runserver
    ```
