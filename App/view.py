﻿"""
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
    pass



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

    if activity is False:
        return (print("\nNo hay datos para el año y sector ingresados\n"))

    return activity.create_table(["Código actividad económica", "Nombre actividad económica","Código subsector económico", "Nombre subsector económico",
                                  "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"	])


def print_req_2(control, code_year, code_sector):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    activity =  controller.req_1(control, code_year, code_sector)

    if activity is False:
        return (print("\nNo hay datos para el año y sector ingresados\n"))

    return activity.create_table(["Código actividad económica", "Nombre actividad económica","Código subsector económico", "Nombre subsector económico",
                                  "Total ingresos netos", "Total costos y gastos","Total saldo a pagar", "Total saldo a favor"])


def print_req_3(control, code_year):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    subsector = controller.req_3(control, code_year)

    if subsector is False:
        return (print( "\nNo hay datos para el año ingresado\n"))

    columns_sector = ["Código sector económico",
                        "Nombre sector económico",
                        "Código subsector económico",
                        "Nombre subsector económico",
                        "Total de retenciones",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    columns_activity = ["Código actividad económica",
                        "Nombre actividad económica",
                        "Total retenciones",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    subsector_table = subsector.create_table_subsector(columns_sector)
    lists = subsector.create_tables_min_max("total_retencions", columns_activity)

    if type(lists) == tuple:
        min_table = lists[0]
        max_table = lists[1]

        print(subsector_table)
        print(min_table)
        print(max_table)

    else:
        print(subsector_table)
        print(lists)


def print_req_4(control, code_year):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    subsector = controller.req_4(control, code_year)

    if subsector is False:
        return print( "\nNo hay datos para el año ingresado\n")

    columns_sector = ["Código sector económico",
                        "Nombre sector económico",
                        "Código subsector económico",
                        "Nombre subsector económico",
                        "Total de costos y gastos de nómina",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    columns_activity = ["Código actividad económica",
                        "Nombre actividad económica",
                        "Costos y gastos nómina",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    subsector_table = subsector.create_table_subsector(columns_sector)
    lists = subsector.create_tables_min_max("total_costs_and_payroll_expenses", columns_activity)

    if type(lists) == tuple:
        min_table = lists[0]
        max_table = lists[1]

        print(subsector_table)
        print(min_table)
        print(max_table)

    else:
        print(subsector_table)
        print(lists)


def print_req_5(control, code_year):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    subsector = controller.req_5(control, code_year)

    if subsector is False:
        return print( "\nNo hay datos para el año ingresado\n")

    columns_sector = ["Código sector económico",
                        "Nombre sector económico",
                        "Código subsector económico",
                        "Nombre subsector económico",
                        "Total de descuentos tributarios",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    columns_activity = ["Código actividad económica",
                        "Nombre actividad económica",
                        "Descuentos tributarios",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    subsector_table = subsector.create_table_subsector(columns_sector)
    lists = subsector.create_tables_min_max("tax_discounts", columns_activity)

    if type(lists) == tuple:
        min_table = lists[0]
        max_table = lists[1]

        print(subsector_table)
        print(min_table)
        print(max_table)

    else:
        print(subsector_table)
        print(lists)


def print_req_6(control, code_year):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    if controller.req_6(control, code_year) is False:
        return print( "\nNo hay datos para el año ingresado\n")

    sector, max_subsector, min_subsector = controller.req_6(control, code_year)

    columns_sector = ["Código sector económico",
                      "Nombre sector económico",
                      "Total ingresos netos",
                      "Total costos y gastos",
                      "Total saldo a pagar",
                      "Total saldo a favor",
                      "Subsector económico que menos aportó",
                      "Subsector económico que más aportó"]

    columns_subsector = ["Código subsector económico",
                         "Nombre subsector económico",
                         "Total ingresos netos",
                         "Total costos y gastos",
                         "Total saldo a pagar",
                         "Total saldo a favor",
                         "Actividad económica que menos aportó",
                         "Actividad económica que más aportó"]

    table_sector = sector.create_table_sector(columns_sector)
    table_max_subsector = max_subsector.create_table_subsector(columns_subsector, [15,15,15,15,15,15])
    table_min_subsector = min_subsector.create_table_subsector(columns_subsector, [15,15,15,15,15,15])

    print(table_sector)
    print(table_max_subsector)
    print(table_min_subsector)


def print_req_7(control, code_year, code_subsector, top:int):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7

    subsector = controller.req_7(control, code_year, code_subsector)

    if subsector is False:
        return print("\n No hay datos para el año y subsector ingresados\n")

    columns_activity = ["Código actividad económica",
                        "Nombre actividad económica",
                        "Código sector económico",
                        "Nombre sector económico",
                        "Descuentos tributarios",
                        "Total ingresos netos",
                        "Total costos y gastos",
                        "Total saldo a pagar",
                        "Total saldo a favor"]

    table = subsector.create_table_top(columns_activity, top, "total_costs_and_expenses")

    print(table)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista


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
                control = new_controller()
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
                code_year = int(input("Ingrese el año a buscar: "))

                print_req_3(control, code_year)


            elif int(inputs) == 5:
                code_year = int(input("Ingrese el año a buscar: "))

                print_req_4(control, code_year)

            elif int(inputs) == 6:
                code_year = int(input("Ingrese el año a buscar: "))

                print_req_5(control, code_year)

            elif int(inputs) == 7:
                code_year = int(input("Ingrese el año a buscar: "))
                print_req_6(control, code_year)

            elif int(inputs) == 8:
                code_year = int(input("Ingrese el año a buscar: "))
                code_subsector = input("Ingrese el código del subsector a buscar: ")
                top = int(input("Ingrese el número TOP actividades a mostrar: "))
                print_req_7(control, code_year, code_subsector, top)

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
