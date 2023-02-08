class Nodo:
    def __init__(self, valor=None, id=-1):
        self.valor = valor
        self.siguiente = None
        self.id = id

    def getValor(self):
        return str(self.valor)

    def setValor(self, par_valor):
        self.valor = par_valor

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, par_siguiente):
        self.siguiente = par_siguiente


