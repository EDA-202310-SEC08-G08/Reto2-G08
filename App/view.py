"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
#%%
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #CHECK: Llamar la función del controlador donde se crean las estructuras de datos

    control = controller.new_controller()

    return control

def load_data(control, filename):
    """
    Carga los datos
    """
    #CHECK: Realizar la carga de datos
    return controller.load_data(control, filename)


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

#DEPRECATED Funcion a quitarse en la sustentacion
def printchooseCSV():
    print('\nIngrese la representación de los datos que quiere usar: ')
    print(' 1. -small')
    print(' 2. -5pct')
    print(' 3. -10pct')
    print(' 4. -20pct')
    print(' 5. -30pct')
    print(' 6. -50pct')
    print(' 7. -80pct')
    print(' 8. -large')

#DEPRECATED Funcion a quitarse en la sustentacion

def fileChoose():
    """

    Da opciones al usuario para que escoja la representación de los datos de su preferencia

    Returns:

        El sufijo de la representación de los datos escogida
    """
    fileChoose = False
    while fileChoose == False:

        suffixFileChoose = input('Opción seleccionada: ')
        if int(suffixFileChoose[0]) == 1:
            suffix = '-small'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 2:
            suffix = '-5pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 3:
            suffix = '-10pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 4:
            suffix = '-20pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 5:
            suffix = '-30pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 6:
            suffix = '-50pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 7:
            suffix = '-80pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 8:
            suffix = '-large'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True

    return suffix

def printHeader(rqn, msg_rq, msg_answer):
    """
    Imprime en consola los encabezados de cada requerimiento

    Args:
        rqn (_type_):   Numero del requerimiento
        msg_rq (_type_): Mensaje del requerimiento (Inputs)
        msg_answer (_type_): Mensaje de Respuesta
    """
    print("\n============= Req No. " + str(rqn) + " Inputs =============")
    print(msg_rq)
    print("\n============= Req No. " + str(rqn) + " Answer =============" )
    print(msg_answer)
    print("------------------------------------------------------------------------")

    return control

def print_charge_data(control):
    columns = ['Año',
               'Código actividad económica',
               'Nombre actividad económica',
               'Código sector económico',
               'Nombre sector económico',
               'Código subsector económico',
               'Nombre subsector económico',
               'Total ingresos netos',
               'Total costos y gastos',
               'Total saldo a pagar',
               'Total saldo a favor',
               ]
    map_by_years = control['model']['map_by_year']

    years = mp.keySet(map_by_years)
    years = controller.sort(years)

    for year in lt.iterator(years):

        entry = mp.get(map_by_years, year)
        data = me.getValue(entry)["data"]

        if lt.size(data) < 6:
            print(f'\nThere are only {lt.size(data)} actividades economicas in {year}\n')
            print(simple_table(data, column_names=columns))
        else:
            print(f"\nThere are {lt.size(data)} actividades economicas in {year}\n")
            print(first_and_last(data, column_names=columns, n=3))



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, code_year, code_sector):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1


    activity =  controller.req_1(control, code_year, code_sector)

    return activity.create_table(["Código actividad económica", "Nombre actividad económica","Código subsector económico", "Nombre subsector económico",
                                  "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"	])


def print_req_2(control, code_year, code_sector):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    activity =  controller.req_1(control, code_year, code_sector)

    return activity.create_table(["Código actividad económica", "Nombre actividad económica","Código subsector económico", "Nombre subsector económico",
                                  "Total ingresos netos", "Total costos y gastos","Total saldo a pagar", "Total saldo a favor"])


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

#ADD Funcion para imprimir los datos en tablas (Tabulate)

def new_element(element, column_names):
    """
    Crea un nuevo elemento para agregar a la tabla
    """
    new_element = {}
    for column in column_names:
        new_element[column] = element[column]

    return list(new_element.values())

def first_and_last(lst, n, column_names):
    table = []

    start_list = lt.subList(lst, 1, n)
    end_list = lt.subList(lst, lt.size(lst)-n+1, n)

    for element in lt.iterator(start_list):
        element = new_element(element, column_names)
        table.append(element)
    for element in lt.iterator(end_list):
        element = new_element(element, column_names)
        table.append(element)

    return tabulate(table, tablefmt="grid", maxcolwidths=20, headers=column_names)

def simple_table(lst, column_names):

    table = []

    for element in lt.iterator(lst):
        element = new_element(element, column_names)
        table.append(element)

    return tabulate(table, tablefmt="grid", maxcolwidths=20, headers=column_names)



# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                #DEPRECATED Funciones a quitarse en la sustentacion por que se confunde el usuario
                printchooseCSV()
                suffix = fileChoose()
                print("Cargando información de los archivos ....\n")
                analyze = load_data(control, suffix)
                all_size = control["model"].all_data.size()
                msg1 = f"Carga de datos con archivo {suffix}"
                msg2 = f"Se cargaron {all_size} datos de los archivos"
                
            elif int(inputs) == 2:
                code_year = int(input("Ingrese el año a buscar: "))
                code_sector = input("Ingrese el código del sector a buscar: ")

                print_req_1(control, code_year, code_sector)

            elif int(inputs) == 3:
                code_year = int(input("Ingrese el año a buscar: "))
                code_sector = input("Ingrese el código del sector a buscar: ")
                print_req_2(control, code_year, code_sector)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")

            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)

# %%
