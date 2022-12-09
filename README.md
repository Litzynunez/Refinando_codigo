# Refinando codigo
 Este es un programa para representar el reporte de ventas de frutas, para visualizar que tanto se ha se ha vendido y que los costos de dichas frutas por libra.


1. **Introducción:** 

En esta asignacion realizamos un repositorio a traves de la plataforma de Github. Siendo de esta forma realizar el ejercicio de "Refinando codigo" de la actividad llamada "PP5, Calidad y archivos". El objetivo de esta asignacion es limpiar nuestro codigo usando diversas herramientas como autopep8 y pylint. Ya despues que hayamos realizado dichas actividades vamos a subirlo automaticamente a un repositorio de Github.


2. **Refactorización:** 

Nuestro procedimiento fue el siguiente: uestro primer paso fue crear la funcion el cual esta convierte el archivo externo (csv) a una lista, utilizando las herramientas como open() y se guarde la variable que luego esta retorne nuevamente al usuario. Despues de este paso, vamos al segundo paso que luego de que se hiciera esta segunda funcion que toma como parametro la variable de la primera funcion para despues sumar todos los valores que estan en nuestra lista. Y para finalizar con el tercer paso de nuestra tercera funcion es la principal, la cual es llamar a las dos funciones que realizamos anteriormente e imprime nuestro resultado final.


3. **Limpieza:** 

Para poder limpiar nuestra codigo, primero tuvimos que usar pylint que es para conseguir una puntuacion del trabajo realizado y nos refleja por igual los siguientes errores que debemos arreglar. Por ende, la mayoria de estos errores son para agregar los docstrings a las funciones al igual que agregar los datos como el de encoding a la hora de abrir nuestro archivo. Cuando finalice de utilizar el pylint y conocer mi puntuacion al igual que corregir mis errores, luego utilizo autopep8 para formatear el trabajo al modo designado, para que despues copie el resultado.


4. **Gestion y control de errores:** 

A la hora ya de ejecutar nuestro codigo, los errores que se visualizaron cuando utilizamos 'with open()' para abrir el archivo en donde se encuentran los precios para arreglarlo. Desde que ya lo arreglamos y cambiamos al formato de la funcion y algunos de los errores de la indentacion. Aparte de realizar esto, uno de los eorres que pude encontrar cuando cree la funcion principal en el 'main()' en la que no podia esta imprimir la respuesta correcta, por ende, lo tuve que arreglar al hacer ya la segunda funcion 'tota()' y tome como parametro la primera funcion 'costs_lits()'.


5. **Pruebas unitarias:** 

Cada una de las pruebas realizadas, utilizamos la herramienta de pytest. En la primera prueba la utilice para poder verficar la lista de precios y esta este de forma correcta. Ya a la hora de realizar la segunda prueba, la utilice para confirmar el costo total este correcto. Y para mi tercera prueba, que fue la ultima, se uso para poder confirmar que la funcion principal este realizado de la forma correcta y no devuelva ningun otro dato. Solamente el resultado de las dos funciones que realizamos anteriormente.


`pylint`.
