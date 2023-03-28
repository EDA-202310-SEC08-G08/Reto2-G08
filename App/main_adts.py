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
 """
 
import config as cf
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

class List:
    
    def __init__(self, datastructure = "SINGLE_LINKED", cmpfunction = None, adt = None):
        
        if adt is not None:
            self.list = adt
        else:
            self.list = lt.newList(datastructure, cmpfunction)
        
        self.datastructure = datastructure
        self.cmpfunction = cmpfunction
        self.sorted = False
        
        if datastructure == "ARRAY_LIST":
            self.elements = self.list["elements"]
        else:
            self.elements = self.list["first"]

    
    def __str__(self) -> str:

        if self.datastructure == "ARRAY_LIST":
            return str(self.elements)
        else:
            return str(self.list["first"])
    
    def __len__(self) -> int:
        return lt.size(self.list)
    
    def __iter__(self):
        return lt.iterator(self.list)
    
    def __type__(self):
        return f"ADT : list , Datastructure: {self.datastructure}"
    
    def addFirst(self, element):
        
        lt.addFirst(self.list, element)
    
    def addLast(self, element):
        
        lt.addLast(self.list, element)
    
    def isEmpty(self) -> bool:
        
        return lt.isEmpty(self.list)
    
    def size(self) -> int:
        return lt.size(self.list)
    
    
    def firstElement(self):
        
        return lt.firstElement(self.list)
    
    def lastElement(self):
        
        return lt.lastElement(self.list)
    
    def getElement(self, pos):
        
        return lt.getElement(self.list, pos)
    
    def deleteElement(self, pos):
        
        return lt.deleteElement(self.list, pos)
    
    def removeFirst(self):
        
        return lt.removeFirst(self.list)
    
    def removeLast(self):
        
        return lt.removeLast(self.list)
    
    def insertElement(self, element, pos):
        
        return lt.insertElement(self.list, element, pos)
    
    def isPresent(self, element):
        
        return lt.isPresent(self.list, element)
    
    def exchange(self, pos1, pos2):
        
        return lt.exchange(self.list, pos1, pos2)
    
    def changeInfo(self, pos, element):
        
        return lt.changeInfo(self.list, pos, element)
    
    def subList(self, pos1, numElements):
        
        return lt.subList(self.list, pos1, numElements)
    
    def iterator(self):
        
        return lt.iterator(self.list)
    
    #OPTIMIZE Algoritmos de Ordenamiento
    #NOTE Se agregan los algoritmos de ordenamiento para listas

    def sort(self, sort_criteria = None):
        #CHANGED No es posible ordenar con una funcion de comparacion comun de una lista
        #        Por ende se debe especificar un criterio de ordenamiento
        if sort_criteria is None:
            return "No se ha especificado un criterio de ordenamiento"

        sorted_list = merg.sort(self.list, sort_criteria)

        self.sorted = True

        return sorted_list

    def isSorted(self, search_function: function):

        if self.sorted:

            return search_function(*args)

        else:

            return "La lista no esta ordenada"


    #OPTIMIZE Algoritmos de Busqueda

    @isSorted
    def linealSearch(self,element,parameter):
        pos = None
        while pos == None:
            for list_element in self.list:
                if lt.getElement(self.list,album_pos)[parameter] == element:
                    pos = album_pos
                    break
            element += 1
        return pos

    @isSorted
    def binarySearch(self, element, parameter):
        """
        Busqueda Binaria de un elemento en una lista ordenada ascendentemente
        Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
        """
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        while i <= f and not found:
            # calcular la posicion de la mitad entre i y f
            m = (i + f) // 2
            if lt.getElement(self.list, m)[parameter] == element:
                pos = m
                found = True
            elif lt.getElement(self.list, m)[parameter] > element:
                f = m - 1
            else:
                i = m + 1
        return pos

    @isSorted
    def binarySearchMin(self, element, parameter):
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        while i <= f and not found:
            m = (i + f) // 2
            if lt.getElement(self.list, m)[parameter] == element:
                pos = m
                found = True
            elif lt.getElement(self.list, m)[parameter] > element:
                f = m - 1
            else:
                i = m + 1
        if found == True:
            while lt.getElement(self.list, pos - 1)[parameter] == element:
                pos -= 1
        elif lt.getElement(self.list, m)[parameter] > element:
            pos = m
            while lt.getElement(self.list, pos - 1)[parameter] > element:
                pos -= 1
        return pos

    @isSorted
    def binarySearchMax(self, element, parameter):
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        while i <= f and not found:
            m = (i + f) // 2
            if lt.getElement(self.list, m)[parameter] == element:
                pos = m
                found = True
            elif lt.getElement(self.list, m)[parameter] > element:
                f = m - 1
            else:
                i = m + 1
        if found == True:
            while lt.getElement(self.list, pos + 1)[parameter] == element:
                pos += 1
        elif lt.getElement(self.list, m)[parameter] < element:
            pos = m
            while lt.getElement(self.list, pos + 1)[parameter] > element:
                pos += 1
        return pos

class Stack:
    
    def __init__(self, datastructure = "DOUBLE_LINKED") -> object:

        self.stack = st.newStack(datastructure)
        self.datastructure = datastructure
    

    def __str__(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def __len__(self) -> int:

        return st.size(self.stack)

    def __type__(self) -> str:

        return f"ADT : stack , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def push(self, element):

        st.push(self.stack, element)

    def pop(self):

        return st.pop(self.stack)

    def isEmpty(self) -> bool:

        return st.isEmpty(self.stack)

    def top(self):

        return st.top(self.stack)

    def size(self) -> int:

        return st.size(self.stack)

class Queue:

    def __init__(self, datastructure)-> object:

        self.queue = qu.newQueue(datastructure)
        self.datastructure = datastructure
        

    def __str__(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])
    def __len__(self) -> int:

        return qu.size(self.queue)

    def __type__(self) -> str:

        return f"ADT : queue , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])
    def enqueue(self, element):

        qu.enqueue(self.queue, element)

    def dequeue(self):

        return qu.dequeue(self.queue)
    def peek(self):

        return qu.peek(self.queue)

    def isEmpty(self) -> bool:

        return qu.isEmpty(self.queue)
    def size(self) -> int:

        return qu.size(self.queue)

class HashMap():

    def __init__(self, numelements=17, maptype = "CHAINING", loadfactor = 4.0, cmpfunction = None):

        self.map = mp.newMap(numelements=numelements, maptype=maptype, loadfactor=loadfactor, cmpfunction=cmpfunction)
        self.maptype = maptype
        self.loadfactor = loadfactor
        self.cmpfunction = cmpfunction
        

    def __str__(self) -> str:

        return str(mp.keySet(self.map))

    def __len__(self) -> int:

        return mp.size(self.map)

    def type(self) -> str:

        return f"ADT : map , Datastructure: {self.maptype}"

    def put(self, key, value):

        mp.put(self.map, key, value)

    def get(self, key):

        return mp.get(self.map, key)

    def remove(self, key):

        return mp.remove(self.map, key)

    def contains(self, key):

        return mp.contains(self.map, key)

    def isEmpty(self) -> bool:

        return mp.isEmpty(self.map)

    def size(self) -> int:

        return mp.size(self.map)

    def keySet(self):

        return mp.keySet(self.map)

    def valueSet(self):

        return mp.valueSet(self.map)        
