from typing import ClassVar
from AnalizadorLexico import AnalizadorLexico
from Error import Error
from Token import Token
from Expresiones import *
from Instrucciones import*
cadena=''
class AnalizadorSintactico:
    def __init__(self):
        self.ListaTokens = []
        self.ListaTokensBien=[]
        self.listaErrores = []
        self.i=0

    def ImpErrores(self):
        if len(self.listaErrores) == 0:
            print('No hubo errores')
        else:
            print("LISTA DE ERRORES")
            for e in self.listaErrores:
                e.impError()

#epsilon
    def epsilon(self):
        return InstruccionEpsilon()

#CursoPorNombre
    def val_red(self):
        if self.ListaTokens[self.i].tipo == 'CADENA' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_generarRed(self):
        if self.ListaTokens[self.i].tipo == 'generarRed' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_red()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))


#IMPRIMIR_LN                             
    def val_imprimirln(self):
        if self.ListaTokens[self.i].tipo == 'CADENA' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'ENTERI' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'ParentesisC' :
            print()
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_imprimirln(self):
        if self.ListaTokens[self.i].tipo == 'consolaln' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_imprimirln()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimirLn(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#IMPRIMIR
    def val_imprimir(self):
        if self.ListaTokens[self.i].tipo == 'CADENA' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'ENETERO' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_imprimir(self):
        if self.ListaTokens[self.i].tipo == 'consola' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_imprimir()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#CursoPorNombre
    def val_PorNombre(self):
        if self.ListaTokens[self.i].tipo == 'CADENA' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_cursoNombre(self):
        if self.ListaTokens[self.i].tipo == 'cursoPorNombre' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_PorNombre()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#CursoPostrequisito
    def val_PreR(self):
        if self.ListaTokens[self.i].tipo == 'ENTERO' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_cursoPre(self):
        if self.ListaTokens[self.i].tipo == 'cursosPrerrequisitos' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_PreR()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#CursoPostrequisito
    def val_PostR(self):
        if self.ListaTokens[self.i].tipo == 'ENTERO' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_cursoPost(self):
        if self.ListaTokens[self.i].tipo == 'cursosPostrrequisitos' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_PostR()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))



#CursoPorCodigo
    def val_PorCodigo(self):
        if self.ListaTokens[self.i].tipo == 'ENTERO' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_cursoCodigo(self):
        if self.ListaTokens[self.i].tipo == 'cursoPorCodigo' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_PorCodigo()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#CursoPorSemestre
    def val_PorSemestre(self):
        if self.ListaTokens[self.i].tipo == 'ENTERO' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_cursoSemestre(self):
        if self.ListaTokens[self.i].tipo == 'cursoPorSemestre' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_PorSemestre()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'PUNTO_COMA' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))



#CREAR CURSO

    def ValPre(self):
        if self.ListaTokens[self.i].tipo=='entero':
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('entero',lexema)
            self.i+=1
            return exp
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def Lista_Pre2(self):
        if self.ListaTokens[self.i].tipo=='COMA':
            self.i+=1
            exp=self.ValPre()
            lista=self.Lista_Pre2()
            return InstruccionListaVaLPre2(exp,lista)
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))    

    def Lista_Pre(self):
        if self.ListaTokens[self.i].tipo=='CorcheteA':
            self.i+=1
            exp=self.ValPre()
            lista=self.Lista_Pre2()
            if self.ListaTokens[self.i].tipo=='CorcheteC':
                self.i += 1 
                return InstruccionListaValPre(lista)
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def val_curso(self):
        if self.ListaTokens[self.i].tipo == 'CADENA' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('cadena',lexema)
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'ENTERO' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('entero',lexema)
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'CorcheteA' :
            lista=self.Lista_Pre()
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def lista_val_crear2(self):
        if self.ListaTokens[self.i].tipo == 'ParentesisC' :
            pass
        elif self.ListaTokens[self.i].tipo == 'COMA' :
            self.i += 1
            exp=self.val_curso()
            lista=self.lista_val_crear2()
            return InstruccionListaValRegistros2(exp,lista)
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def lista_val_crear(self):
        exp=self.val_curso()
        lista=self.lista_val_crear2()
        return InstruccionListaValRegistros(exp,lista)

    def Curso(self):
        lista=self.lista_val_crear()
        return lista

    def ins_CrearCurso(self):
        if self.ListaTokens[self.i].tipo == 'crearcurso' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                lista=self.Curso()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    return InstruccionRegistro(lista)
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
        else:
            self.listaErrores.append(Error("Se esperaba crearcurso","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))



#GENERALES
    def instruccion(self):
        if self.ListaTokens[self.i].tipo=="crearcurso":
            ins=self.ins_CrearCurso()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'consolaln' :
            ins=self.ins_imprimirln()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'consola' :
            ins=self.ins_imprimir()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'cursoPorNombre' :
            ins=self.ins_cursoNombre()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'cursoPorCodigo' :
            ins=self.ins_cursoCodigo()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'cursosPorSemestre' :
            ins=self.ins_cursoSemestre()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'cursosPrerrequisitos' :
            ins=self.ins_cursoPre()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'cursosPostrrequisitos' :
            ins=self.ins_cursoPost()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'generarRed' :
            ins=self.ins_generarRed()
            return InstruccionInstruccion(ins)

        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].lexema+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))

    def Lista_Instrucciones2(self):
        if self.ListaTokens[self.i].tipo=="crearcurso":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="EOF":
            ins=self.epsilon()
            print("Analisis Sintactico exitoso")
            return InstruccionListaInstrucciones2(ins,[])
        elif self.ListaTokens[self.i].tipo=="consolaln":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="consola":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursoPorNombre":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursoPorCodigo":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPorSemestre":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPrerrequisitos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPostrrequisitos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="generarRed":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].lexema+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))
        
    def Lista_Instrucciones(self):
        if self.ListaTokens[self.i].tipo=="crearcurso":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo == 'Registro' :
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()        
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="consolaln":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="consola":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursoPorNombre":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursoPorCodigo":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPorSemestre":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPrerrequisitos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="cursosPostrrequisitos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="generarRed":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].lexema+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))
      
    def inicio(self):
        
        lista=self.Lista_Instrucciones()
        return InstruccionInicio(lista)

    def analizar(self,Lista):
        global cadena
        print(cadena)
        self.i=0
        self.ListaTokens=Lista
        arbol=self.inicio()
        if len(self.listaErrores)==0:
            #arbol.ejecutar({})
            #arbol.getNodos()
            c=cadenas()
            cadena=c.Getearxd()
            #print(cadena)
        else:
            cadena="¡¡¡ERROR SINTACTICO!!!\n"+self.listaErrores[0].descripcion+" en linea "+ str(self.listaErrores[0].linea)+" columna "+str(self.listaErrores[0].columna)
        return cadena
