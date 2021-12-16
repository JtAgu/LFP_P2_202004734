from graphviz import Graph


dot = Graph('arbol', 'png')
dot.format = 'png'
dot.attr(splines = 'false')
dot.node_attr.update(shape = 'circle')
dot.edge_attr.update(color = 'black')

i = 0

def Inicio():
    global i
    i += 1
    return i


class ExpresionLiteral():
    def __init__(self,tipo,valor):
        self.valor=valor

    def getValor(self,entorno):
        return self.valor

    def getNodos(self):
        global dot
        idnodo = str(Inicio())
        dot.node(idnodo, 'expresion')
        
        idlit = str(Inicio())
        dot.node(idlit, 'literal')

        idexp = str(Inicio())
        dot.node(idexp, self.valor)

        dot.edge(idlit, idexp)
        dot.edge(idnodo, idlit)

        return idnodo

        