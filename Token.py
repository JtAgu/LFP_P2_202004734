class Token:
    def __init__(self, lexema, tipo,  linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.linea = linea 
        #if self.tipo == 'pensum' or self.tipo == 'curso' or self.tipo == 'codigo' or self.tipo == 'nombre' or self.tipo == 'requisitos':
        #    self.color = 'azul' #azul
        #elif self.tipo == 'llavea' or self.tipo == 'llavec' or self.tipo == 'dospuntos' or self.tipo == 'puntocoma' or self.tipo == 'coma':
        #    self.color = 'rosado' #rosado
        #elif self.tipo == 'cadena':
        #    self.color = 'verde' #verde
        #elif self.tipo == 'entero':
        #    self.color = 'amarillo' #amarillo

        if self.tipo == 'TITULO' or self.tipo == 'ANCHO' or self.tipo == 'ALTO' or self.tipo == 'FILAS' or self.tipo == 'COLUMNAS' or self.tipo=="CELDAS"or self.tipo=="FILTRO" or self.tipo=="nombre":
            self.color = '\033[4;34m' #azul
        elif self.tipo == 'LlaveA' or self.tipo == 'LlaveC' or self.tipo == 'dospuntos' or self.tipo == 'puntocoma' or self.tipo == 'coma' or self.tipo=="CorcheteA"or self.tipo=="CorcheteC" or self.tipo=="espacio"or self.tipo=="igual":
            self.color = '\033[4;35m' #rosado
        elif self.tipo == 'colorear':
            self.color = '\033[4;32m' #verde
        elif self.tipo == 'entero':
            self.color = '\x1b[1;33m' #amarillo
        elif self.tipo == 'error':
            self.color = '\033[4;31m' #rojo

    def impToken(self):
        #print(self.color +' ' , self.lexema, self.tipo, self.linea, self.columna)
        print(self.lexema, self.tipo, self.linea, self.columna)