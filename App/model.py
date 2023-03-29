"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import main_adts as adt
import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(maptype, loadfactor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #CHECK: Inicializar las estructuras de datos
    data_structs = {
        "all_data": None,
    }

    #NOTE Lista de los datos "brutos" con toda la informacion desordenada
    data_structs["all_data"] = lt.newList(datastructure="ARRAY_LIST", cmpfunction=cmp_by_id)

    data_structs["map_by_year"] = mp.newMap(numelements=10,
                                            maptype=maptype,
                                            loadfactor=loadfactor,)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    d = new_data(data)
    lt.addLast(data_structs["all_data"], d)
    add_register_by_year(data_structs, data)

    return data_structs

def add_register_by_year(data_structs, data):

    map_by_year = data_structs["map_by_year"]

    year = data["Año"]

    exist = mp.contains(map_by_year, year)

    if not exist:

        value = new_year(year)
        mp.put(map_by_year, year, value)
        entry = mp.get(map_by_year, year)
        year_data = me.getValue(entry)["data"]
        lt.addLast(year_data, data)
    else:
        entry = mp.get(map_by_year, year)
        year_data = me.getValue(entry)["data"]
        lt.addLast(year_data, data)

    return data_structs

# Funciones para creacion de datos

def new_data(info):
    """
    Crea una nueva estructura para modelar los datos
    """
    try:
        info["id"] = int(info["Año"] + info['Código actividad económica'])
    except:
        i = 0
        for char in info["Código actividad económica"]:
            if char in [" ","/"]:
                info["Código actividad económica"] = info["Código actividad económica"][0:i]
                break
            else:
                i += 1
        info["id"] = int(info["Año"] + info["Código actividad económica"])

    return info

def new_year(year):

    structure = {'year': year,
                 'data' : None}

    structure['data'] = lt.newList(datastructure="ARRAY_LIST", cmpfunction=cmp_by_id)

    return structure

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


#NOTE Funciones utilizadas para comparar elementos dentro de una lista

def cmp_by_id(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

#NOTE Funciones utilizadas para comparar las llaves dentro de un mapa


def compare_map_keys(year, entry):
    """
    Compara dos llaves de un mapa
    """

    year_key = me.getKey(entry)

    if (int(year) == int(year_key)):
        return 0
    elif (int(year) > int(year_key)):
        return 1
    else:
        return -1

#NOTE Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sc_by_element(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1 > data_2:
        return False
    else:
        return True



def sort(lst, sort_criteria):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento

    ordered_list = merg.sort(lst, sort_criteria)

    return ordered_list

#OPTIMIZE Objectos


class DataStructs:

    def __init__(self):

        self.all_data = None
        self.map_by_year = None

class EconomicActivity:

    def __init__(self, data: dict):

        """
        This method initializes an object with attributes from a data dictionary.

        Parameters:
        data (dict): A dictionary containing information about an economic activity.

        Attributes:
        year (int): The year of the activity.
        code_activity (str): The code of the economic activity.
        name_activity (str): The name of the economic activity.
        code_subsector (str): The code of the economic subsector.
        name_subsector (str): The name of the economic subsector.
        code_sector (str): The code of the economic sector.
        name_sector (str): The name of the economic sector.
        total_net_incomes (float): The total net incomes of the activity.
        total_favorable_balance (float): The total favorable balance of the activity.
        total_payable_balance (float): The total payable balance of the activity.
        total_retencions (float): The total retentions of the activity.
        total_cost_and_expenses (float): The total cost and expenses of the activity.
        total_costs (float): The total costs of the activity.
        costs (dict): A dictionary containing the breakdown of costs by category.
        costs_and_payroll_expenses (float): The total costs and payroll expenses of the activity.
        tax_discounts (float): The total tax discounts of the activity.

        """

        self.year = data["Año"]
        self.code_activity = data["Código actividad económica"]
        self.name_activity = data["Nombre actividad económica"]
        self.code_subsector = data["Código subsector económico"]
        self.name_subsector = data["Nombre subsector económico"]
        self.code_sector = data["Código sector económico"]
        self.name_sector = data["Nombre sector económico"]
        self.total_net_incomes = data["Total ingresos netos"]
        self.total_favorable_balance = data["Total saldo a favor"]
        self.total_payable_balance = data["Total saldo a pagar"]
        self.total_retencions = data["Total retenciones"]
        self.total_cost_and_expenses = data["Total costos y gastos"]
        self.total_costs = data["Total costos"]
        self.costs = data["Costos"]
        self.costs_and_payroll_expenses = data["Costos y gastos nómina"]
        self.tax_discounts = data["Descuentos tributarios"]








