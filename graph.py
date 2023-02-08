import graphviz

class graphvizImage:
    def __init__(self):
        self.dot = graphviz.Digraph('structs', filename='structs.gv',
                                    node_attr={'shape': 'record'})

    def addNodoDot(self, nodoInicio, nodosiguiente):
        if(nodosiguiente !=None):
            self.dot.node(str(nodoInicio.id), str(nodoInicio.valor))
            self.dot.node(str(nodosiguiente.id), str(nodosiguiente.valor))
            self.dot.edge(str(nodoInicio.id), str(nodosiguiente.id))

    def generar(self):
        self.dot.render(directory='img').replace('\\', '/')
        'img/structs.pdf'