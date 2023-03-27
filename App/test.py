import controller
import model
from tabulate import tabulate
import main_adts as adt
from DISClib.DataStructures import mapentry as me

def new_controller(maptype, loadfactor):
    """
        Se crea una instancia del controlador
    """
    #CHECK: Llamar la función del controlador donde se crean las estructuras de datos

    control = controller.new_controller(maptype,loadfactor)

    return control

def memory_and_time():
    """
    Retorna el tiempo y la memoria utilizada por el programa
    """


    table_probing = []
    table_chaining = []
    loadfactor_probing = [0.1,0.5, 0.7, 0.9]
    loadfactor_chaining = [2,4,6,8]


    for i in loadfactor_probing:

        control = new_controller("PROBING", i)
        analyze = controller.load_data(control, "-large.csv", True)
        time = controller.load_data(control, "-large.csv", False)
        row = [i, time, analyze[1]]
        table_probing.append(row)

    for i in loadfactor_chaining:

        control = new_controller("CHAINING", i)
        analyze = controller.load_data(control, "-large.csv", True)
        time = controller.load_data(control, "-large.csv", False)
        row = [i, time, analyze[1]]
        table_chaining.append(row)

    return table_probing, table_chaining

def print_results(table_probing, table_chaining):
    print("Tabla de tiempos y memoria para el tipo de tabla Hashing: Probing")
    print(tabulate(table_probing, headers=["Load Factor", "Tiempo", "Memoria"], tablefmt="fancy_grid"))
    print("Tabla de tiempos y memoria para el tipo de tabla Hashing: Chaining")
    print(tabulate(table_chaining, headers=["Load Factor", "Tiempo", "Memoria"], tablefmt="fancy_grid"))


def test_hash():
    table_probing, table_chaining = memory_and_time()
    print_results(table_probing, table_chaining)


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

my_map = adt.HashMap(3, "CHAINING", 4, compare_map_keys)

my_map.put("2018", "Hola 2018")
my_map.put("2019", "Hola 2019")
my_map.put("2020", "Hola 2020")
my_map.put("2021", "Hola 2021")

print(my_map.maptype)

print(my_map.get("2018"))

print(type(my_map))

my_map.remove("2018")

str(my_map)

print(my_map.contains("2018"))
print(my_map.contains("2019"))

print(my_map.size())
print(len(my_map))

print(my_map.type())





                



