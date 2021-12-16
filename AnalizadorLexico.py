from Token import Token
from Error import Error
import re

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analizar(self, codigo_fuente):
        self.listaTokens = []
        self.listaErrores = []

        #inicializar atributos
        linea = 1
        columna = 1
        buffer = ''
        centinela = '#'
        estado = 0
        
        #automata
        i = 0

        while i< len(codigo_fuente):
            c = codigo_fuente[i]

            if estado == 0:
                if c==" ":
                    columna += 1

                elif c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'IGUAL', linea, columna))    
                    buffer = ''
                    columna += 1
                    
                elif c == '(':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'ParentesisA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'ParentesisC', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'LlaveA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'LlaveC', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'PUNTO_COMA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'COMA', linea, columna))
                    buffer = ''
                    columna += 1
                                  
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                    
                elif re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                
                elif c == '\'' or c == '"':
                    columna += 1
                    estado = 1
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == '\t':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'ENTERO', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 1:
                if c == '\'' or c == '"':
                    self.listaTokens.append(Token(buffer, 'CADENA', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1

            elif estado == 3:
                if re.search('[a-z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'cursosPrerrequisitos':
                        self.listaTokens.append(Token(buffer, 'REPLIST', linea, columna))
                    elif buffer == 'cursoPorNombre':
                        self.listaTokens.append(Token(buffer, 'NOMBRE', linea, columna))
                    elif buffer == 'cursoPorCodigo':
                        self.listaTokens.append(Token(buffer, 'ARTISTA', linea, columna))
                    elif buffer == 'cursosPorSemestre':
                        self.listaTokens.append(Token(buffer, 'RUTA', linea, columna))
                    elif buffer == 'consolaln':
                        self.listaTokens.append(Token(buffer, 'GENERO', linea, columna))
                    elif buffer == 'consola':
                        self.listaTokens.append(Token(buffer, 'REPETIR', linea, columna))
                    elif buffer == 'crearcurso':
                        self.listaTokens.append(Token(buffer, 'ANIO', linea, columna))
                    elif buffer == 'nombre_de_red':
                        self.listaTokens.append(Token(buffer, 'ANIO', linea, columna))
                    elif buffer == 'cursosPostrrequisitos':
                        self.listaTokens.append(Token(buffer, 'ANIO', linea, columna))
                    elif buffer == 'generarRed':
                        self.listaTokens.append(Token(buffer, 'ANIO', linea, columna))
                    else:
                        self.listaErrores.append(Error(buffer + ' no es reconocido en el lenguaje.', 'Léxico', linea, columna))
                        
                    buffer = ''
                    i -= 1
                    columna += 1
                    estado = 0
            
            i += 1

    def impTokens(self):
        print("LISTA DE TOKENS")
        for t in self.listaTokens:
            t.impToken()

    def impErrores(self):
        if len(self.listaErrores) == 0:
            print('No hubo errores')
        else:
            print("LISTA DE ERRORES")
            for e in self.listaErrores:
                e.impError()