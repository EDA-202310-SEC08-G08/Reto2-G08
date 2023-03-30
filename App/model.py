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
from types import FunctionType
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

#OPTIMIZE Objects

class DataStructs:

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_year = adt.HashMap(numelements=10, maptype="PROBING", loadfactor=0.5)


class Year(DataStructs):

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_sector = adt.HashMap(numelements=15, maptype="PROBING", loadfactor=0.5)


class Sector(Year):

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        self.map_by_subsector = adt.HashMap(numelements=21, maptype="PROBING", loadfactor=0.5)

        #NOTE: Atributos para el requerimiento 1
        self.max_total_payable_balance = None #NOTE: EconomicActivity
        self.min_total_payable_balance = None #NOTE: EconomicActivity
        #NOTE: Atributos para el requerimiento 2
        self.max_total_favorable_balance = None #NOTE: EconomicActivity
        self.min_total_favorable_balance = None #NOTE: EconomicActivity



class Subsector(Sector):

    def __init__(self):

        self.all_data = adt.List(datastructure="ARRAY_LIST", cmpfunction=compare_by_id)
        #NOTE: Atributos para el requerimiento 3
        self.min_total_retencions = None #NOTE: EconomicActivity
        self.max_total_retencions = None #NOTE: EconomicActivity
        #NOTE: Atributos para el requerimiento 4
        self.min_total_costs_and_payroll_expenses = None #NOTE: EconomicActivity
        self.max_total_costs_and_payroll_expenses = None #NOTE: EconomicActivity
        #NOTE: Atributos para el requerimiento 5
        self.min_tax_discounts = None #NOTE: EconomicActivity
        self.max_tax_discounts = None #NOTE: EconomicActivity

        #HACK Atributos para el requerimiento 6
        self.total_net_incomes = 0

    def calculate_max_and_min(self, sort_criteria: FunctionType, attribute: str):
        """
        Función encargada de calcular el máximo y el mínimo de total retenciones
        """

        subsector_all_data = self.all_data

        subsector_all_data.sort(sort_criteria)

        max = subsector_all_data.get(1)

        min = subsector_all_data.get(subsector_all_data.size())

        if attribute == "total_retencions":
            self.min_total_retencions = min
            self.max_total_retencions = max
        elif attribute == "total_costs_and_payroll_expenses":
            self.min_total_costs_and_payroll_expenses = min
            self.max_total_costs_and_payroll_expenses = max
        elif attribute == "tax_discounts":
            self.min_tax_discounts = min
            self.max_tax_discounts = max

        return max, min




class EconomicActivity():

    def __init__(self, data: dict):
        """
        This class represents an economic activity.

        Attributes:
        year (int): The year of the data.
        code_activity (int): The code of the economic activity.
        name_activity (str): The name of the economic activity.
        code_subsector (int): The code of the subsector.
        name_subsector (str): The name of the subsector.
        code_sector (int): The code of the sector.
        name_sector (str): The name of the sector.
        total_net_incomes (int): The total net incomes.
        total_favorable_balance (int): The total favorable balance.
        total_payable_balance (int): The total payable balance.
        total_retencions (int): The total retentions.
        total_cost_and_expenses (int): The total cost and expenses.
        costs (int): The costs.
        costs_and_payroll_expenses (int): The costs and payroll expenses.
        tax_discounts (int): The tax discounts.
        """

        self.year = int(data["Año"])
        self.code_activity = (data["Código actividad económica"])
        self.name_activity = data["Nombre actividad económica"]
        self.code_subsector = (data["Código subsector económico"])
        self.name_subsector = data["Nombre subsector económico"]
        self.code_sector = (data["Código sector económico"])
        self.name_sector = data["Nombre sector económico"]
        self.total_net_incomes = int(data["Total ingresos netos"])
        self.total_favorable_balance = int(data["Total saldo a favor"])
        self.total_payable_balance = int(data["Total saldo a pagar"])
        self.total_retencions = int(data["Total retenciones"])
        self.total_cost_and_expenses = int(data["Total costos y gastos"])
        self.costs = int(data["Costos"])
        self.costs_and_payroll_expenses = int(data["Costos y gastos nómina"])
        self.tax_discounts = int(data["Descuentos tributarios"])

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #CHECK: Inicializar las estructuras de datos


    data_structs = DataStructs()

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs : DataStructs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    d = new_data(data)

    data_structs.all_data.addLast(d)

    add_register_by_year(data_structs, d)

    return data_structs

def add_register_by_year(data_structs : DataStructs, data : EconomicActivity):

    map_by_year = data_structs.map_by_year

    year = data.year

    exist = map_by_year.contains(year)

    if not exist:

        value = Year()
        map_by_year.put(year, value)
        entry = map_by_year.get(year)
        year_data = me.getValue(entry)
        year_data.all_data.addLast(data)
        add_register_by_sector(year_data, data)
    else:
        entry = map_by_year.get(year)
        year_data = me.getValue(entry)
        year_data.all_data.addLast(data)
        add_register_by_sector(year_data, data)

    return data_structs


def add_register_by_sector(year : Year, data : EconomicActivity):

    map_by_sector = year.map_by_sector

    sector = data.code_sector

    exist = map_by_sector.contains(sector)

    if not exist:
        value = Sector()
        map_by_sector.put(sector, value)
        entry = map_by_sector.get(sector)
        sector_data = me.getValue(entry)
        sector_data.all_data.addLast(data)
        add_register_by_subsector(sector_data, data)
    else:
        entry = map_by_sector.get(sector)
        sector_data = me.getValue(entry)
        sector_data.all_data.addLast(data)
        add_register_by_subsector(sector_data, data)

    return year

def add_register_by_subsector(sector : Sector, data : EconomicActivity):

    map_by_subsector = sector.map_by_subsector

    subsector = data.code_subsector

    exist = map_by_subsector.contains(subsector)

    if not exist:
        value = Subsector()
        map_by_subsector.put(subsector, value)
        entry = map_by_subsector.get(subsector)
        subsector_data = me.getValue(entry)
        subsector_data.all_data.addLast(data)
    else:
        entry = map_by_subsector.get(subsector)
        subsector_data = me.getValue(entry)
        subsector_data.all_data.addLast(data)

    return sector

# Funciones para creacion de datos

def new_data(info):
    """
    Crea una nueva estructura para modelar los datos
    """
    # try:
    #     info["id"] = int(info["Año"] + info['Código actividad económica'])
    # except:
    #     i = 0
    #     for char in info["Código actividad económica"]:
    #         if char in [" ","/"]:
    #             info["Código actividad económica"] = info["Código actividad económica"][0:i]
    #             break
    #         else:
    #             i += 1
    #     info["id"] = int(info["Año"] + info["Código actividad económica"])

    # return info

    data = EconomicActivity(info)

    try:
        data.id = int(data.year + data.code_activity)
    except:
        i = 0

        for char in data.code_activity:
            if char in [" ","/"]:
                data.code_activity = data.code_activity[0:i]
                break
            else:
                i += 1
        data.id = int(data.year + int(data.code_activity))

    return data


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

def compare_by_id(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    id_1 = data_1["id"]
    id_2 = data_2["id"]

    if id_1 > id_2:
        return 1
    elif id_1 < id_2:
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


