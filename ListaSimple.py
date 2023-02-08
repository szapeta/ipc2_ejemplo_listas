from nodo import Nodo
from graph import graphvizImage

class ListaSimple:
    static_id = 0
    def __init__(self):
        self.size = 0
        self.root = None
        self.ultimo = None

    def agregar(self, valor):
        self.static_id +=1
        if self.size == 0:
            self.root = Nodo(valor, self.static_id)
            self.ultimo = self.root
        else: #ya existen nodos en la lista
            nototmp = Nodo(valor, self.static_id)
            self.ultimo.setSiguiente(nototmp)
            self.ultimo = nototmp
        self.size += 1


    def agregarPos(self, pos_x):
        pass

    def eliminar(self):
        pass

    def eliminarPos(self, pos_x):
        pass

    def printNodos(self):
        nodoI = self.root
        while(nodoI != None):
            print(nodoI.getValor(), str(nodoI.id))
            nodoI = nodoI.getSiguiente()

    def createGraph(self):
        objGraph = graphvizImage()
        nodoI = self.root
        while (nodoI != None):
            objGraph.addNodoDot(nodoI, nodoI.getSiguiente())
            nodoI = nodoI.getSiguiente()

        objGraph.generar()
