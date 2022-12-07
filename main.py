#########################################################################################################################################################################
# Litzy Nuñez
# 22-0413
# Venta de frutas
# ******Descripcion del problema******
##########################################################################################################################################################################

#Rayitas y espacios
rayitas = "-"*68
espacios = " "*12
#Solicitar al usuario un conjunto de datos
print(rayitas+"\nREPORTE DE VENTAS DE FRUTAS NAVIDEÑAS\n"+rayitas)
lista_datos = []
#probando

def mostrar_menu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'{nombre} \nSeleccione la opción deseada:\n')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Reporte general de ventas', submenu),
        '2': ('Reporte de ventas de pasas', funcion1),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Reporte de ventas de peras', funcion2),
        '4': ('Reporte de ventas de manzanas', funcion3),
        '5': ('Reporte de ventas de uvas', funcion5)
       
    }
    generar_menu(rayitas+'\nMENU PRINCIPAL\n'+rayitas, opciones, '4')  # indicamos el nombre del menú




###CHECKKKKK AÑADIR 1 MAS

def submenu():
    opciones = {
        'a': ('REPORTE GENERAL', funcionA),
        'b': ('Volver al menú principal ', salir),
    }

    generar_menu('Submenú', opciones, 'c')  # indicamos el nombre del submenú


# A partir de aquí creamos las funciones que ejecutan las acciones de los menús
def funcion1():
    print('Has elegido la opcion de REPORTE GENERAL')

def funcion2():
    print('Has elegido la opción 1')


def funcion3():
    print('Has elegido la opción 2')


def funcion4():
    print('Haz elegido el 3')


def funcion5():
     print('Haz elegido el 4')


def funcionA():
    print('Has elegido la opción A')


def funcionB():
    print('Has elegido la opción B')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal() # iniciamos el programa mostrando el menú principal








########PROGRAMA ESENCIAL AÑADIR AL PROGRAMA###########

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = [int(c) for c in gift_costs]  # convierte strings a int

total_price = 0
for cost in gift_costs:
    if cost > 1000:
        total_price += cost * 1.16  # agrega impuestos
    else:
        total_price += cost

print(total_price)

print("\n" + rayitas + "\nVENTAS DE FRUTAS NAVIDEÑAS\n" + rayitas + "\nInformaciones generales" + rayitas)

#####PROGRAMA DE SELECCION###########





