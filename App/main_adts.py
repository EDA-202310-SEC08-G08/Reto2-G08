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
    
    def sort(self, sort_criteria = None):

        if sort_criteria is None:
            sort_criteria = self.cmpfunction

        sorted_list = merg.sort(self.list, sort_criteria)

        return sorted_list

class Stack:
    
    def __init__(self, datastructure = "DOUBLE_LINKED"):

        self.stack = st.newStack(datastructure)
        self.datastructure = datastructure
        self.size = st.size(self.stack)

    def __str__(self) -> str:
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def __len__(self) -> int:

        return st.size(self.stack)

    def __type__(self):

        return f"ADT : stack , Datastructure: {self.datastructure}"

    def elements(self):
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










    

        
        
        
        
    
    
    
        
        
        