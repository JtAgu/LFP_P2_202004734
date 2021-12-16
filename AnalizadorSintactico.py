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

#CLAVES
    def val_claves(self):
        if self.ListaTokens[self.i].tipo=="cadena":
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('cadena',lexema)
            self.i+=1
            return exp
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))

    def Lista_Claves2(self):
        if self.ListaTokens[self.i].tipo=='coma':
            self.i+=1
            ins=self.val_claves()
            lista=self.Lista_Claves2()
            return InstruccionListaClaves2(ins,lista)
        elif self.ListaTokens[self.i].tipo=='CorcheteC':
            pass            
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))
    
    def Lista_Claves(self):
        ex=self.val_claves()
        lista=self.Lista_Claves2()
        return InstruccionListaClaves(ex,lista)

    def ins_Clave(self):
        if self.ListaTokens[self.i].tipo=="Claves":
            self.i+=1
            if self.ListaTokens[self.i].tipo=="igual":
                self.i+=1
                if self.ListaTokens[self.i].tipo=="CorcheteA":
                    self.i+=1
                    lista=self.Lista_Claves()
                    if self.ListaTokens[self.i].tipo=="CorcheteC":                        
                        self.i+=1
                        return InstruccionClave(lista)
                    else:
                        self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#REGISTROS
    def val_reg(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('cadena',lexema)
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'entero' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('entero',lexema)
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'decimal' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('decimal',lexema)
            self.i+=1
            return exp
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def lista_val_reg2(self):
        if self.ListaTokens[self.i].tipo == 'LlaveC' :
            pass
        elif self.ListaTokens[self.i].tipo == 'coma' :
            self.i += 1
            exp=self.val_reg()
            lista=self.lista_val_reg2()
            return InstruccionListaValRegistros2(exp,lista)
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def lista_val_reg(self):
        exp=self.val_reg()
        lista=self.lista_val_reg2()
        return InstruccionListaValRegistros(exp,lista)

    def registro(self):
        if self.ListaTokens[self.i].tipo == 'LlaveA' :
            self.i += 1
            lista=self.lista_val_reg()
            if self.ListaTokens[self.i].tipo == 'LlaveC' :
                self.i += 1
                return lista
            else:
                self.listaErrores.append(Error("Se esperaba }","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
        else:
            self.listaErrores.append(Error("Se esperaba {","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def lista_registros2(self):
        if self.ListaTokens[self.i].tipo == 'CorcheteC' :
            pass
        elif self.ListaTokens[self.i].tipo == 'LlaveA':
            exp=self.registro()
            lista=self.lista_registros2()
            return InstruccionListaRegistros2(exp,lista)
        else:
            pass
    
    def lista_registros(self):
        exp=self.registro()
        lista=self.lista_registros2()
        return InstruccionListaRegistros(exp,lista)

    def ins_registros(self):
        if self.ListaTokens[self.i].tipo == 'Registro' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'igual' :
                self.i += 1
                if self.ListaTokens[self.i].tipo == 'CorcheteA' :
                    self.i += 1
                    lista=self.lista_registros()
                    if self.ListaTokens[self.i].tipo == 'CorcheteC' :
                        self.i += 1 
                        return InstruccionRegistro(lista)
                    else:
                        self.listaErrores.append(Error("Se esperaba ]","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba [","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba =","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#IMPRIMIR_LN                             
    def val_imprimirln(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'entero' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'decimal' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('decimal',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'ParentesisC' :
            print()
        else: 
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].tipo+" no esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_imprimirln(self):
        if self.ListaTokens[self.i].tipo == 'imprimirln' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_imprimirln()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
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
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'entero' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('entero',lexema)
            self.i+= 1
            return expresion
        elif self.ListaTokens[self.i].tipo == 'decimal' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('decimal',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba valor de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_imprimir(self):
        if self.ListaTokens[self.i].tipo == 'imprimir' :
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                expresion=self.val_imprimir()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionImprimir(expresion)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#CONTEO
    def ins_conteo(self):
        if self.ListaTokens[self.i].tipo == 'conteo':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionConteo(ExpresionLiteral("instruccion",0))
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#PROMEDIO
    def val_promedio(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            exp=ExpresionLiteral('cadena',lexema)
            self.i+=1
            return exp
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_promedio(self):
        if self.ListaTokens[self.i].tipo == 'promedio':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_promedio()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionPromedio(exp)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#DATOS
    def ins_datos(self):
        if self.ListaTokens[self.i].tipo == 'datos':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionDatos(ExpresionLiteral("instruccion",0))
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#SUMAR
    def val_sumar(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_sumar(self):
        if self.ListaTokens[self.i].tipo == 'sumar':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_sumar()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionSumar(exp)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#MAXIMO
    def val_max(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_max(self):
        if self.ListaTokens[self.i].tipo == 'max':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_max()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionMax(exp)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#MINIMO
    def val_min(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadenas',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_min(self):
        if self.ListaTokens[self.i].tipo == 'min':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_max()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionMin(exp)
                    else:
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
    
#CONTAR SI
    def val_contarsi2(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            exp=lexema
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'entero' :
            lexema=self.ListaTokens[self.i].lexema
            exp=lexema
            self.i+=1
            return exp
        elif self.ListaTokens[self.i].tipo == 'decimal' :
            lexema=self.ListaTokens[self.i].lexema
            exp=lexema
            self.i+=1
            return exp
        else: 
            self.listaErrores.append(Error("Se esperaba dato de entrada","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def val_contarsi(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            exp=lexema
            self.i+=1
            if self.ListaTokens[self.i].tipo == 'coma':
                self.i+= 1
                exp2=self.val_contarsi2()
                expresion=exp+','+exp2
                return ExpresionLiteral('lista',expresion)
            else: 
                self.listaErrores.append(Error("Se esperaba ,","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_contarsi(self):
        if self.ListaTokens[self.i].tipo == 'contarsi':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_contarsi()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionContarSi(exp)
                    else: 
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
                else: 
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else: 
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#REPORTE                        
    def val_reporte(self):
        if self.ListaTokens[self.i].tipo == 'cadena' :
            lexema=self.ListaTokens[self.i].lexema
            expresion=ExpresionLiteral('cadena',lexema)
            self.i+= 1
            return expresion
        else: 
            self.listaErrores.append(Error("Se esperaba cadena","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

    def ins_reporte(self):
        if self.ListaTokens[self.i].tipo == 'reporte':
            self.i += 1
            if self.ListaTokens[self.i].tipo == 'ParentesisA' :
                self.i += 1
                exp=self.val_reporte()
                if self.ListaTokens[self.i].tipo == 'ParentesisC' :
                    self.i += 1 
                    if self.ListaTokens[self.i].tipo == 'puntocoma' :
                        self.i += 1 
                        return InstruccionReporte(exp)
                    else: 
                        self.listaErrores.append(Error("Se esperaba ;","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

                else:
                    self.listaErrores.append(Error("Se esperaba )","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
            else:
                self.listaErrores.append(Error("Se esperaba (","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))
        else:
            self.listaErrores.append(Error("Se esperaba reporte","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna+1))

#epsilon
    def epsilon(self):
        return InstruccionEpsilon()

#GENERALES
    def instruccion(self):
        if self.ListaTokens[self.i].tipo=="Claves":
            ins=self.ins_Clave()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'Registro' :
            ins=self.ins_registros()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'imprimirln' :
            ins=self.ins_imprimirln()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'imprimir' :
            ins=self.ins_imprimir()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'promedio' :
            ins=self.ins_promedio()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'conteo' :
            ins=self.ins_conteo()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'datos' :
            ins=self.ins_datos()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'sumar' :
            ins=self.ins_sumar()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'max' :
            ins=self.ins_max()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'min' :
            ins=self.ins_min()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'contarsi' :
            ins=self.ins_contarsi()
            return InstruccionInstruccion(ins)

        elif self.ListaTokens[self.i].tipo == 'reporte' :
            ins=self.ins_reporte()
            return InstruccionInstruccion(ins)    
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].lexema+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))

    def Lista_Instrucciones2(self):
        if self.ListaTokens[self.i].tipo=="Claves":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="EOF":
            ins=self.epsilon()
            print("Analisis Sintactico exitoso")
            return InstruccionListaInstrucciones2(ins,[])
        elif self.ListaTokens[self.i].tipo=="imprimirln":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="imprimir":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="conteo":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="promedio":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="contarsi":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="datos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="sumar":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="max":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="min":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="Registro":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        elif self.ListaTokens[self.i].tipo=="reporte":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones2(ins,lista)
        else:
            self.listaErrores.append(Error("Token "+self.ListaTokens[self.i].lexema+" NO era el esperado","Sintactico",self.ListaTokens[self.i].linea,self.ListaTokens[self.i].columna))
        
    def Lista_Instrucciones(self):
        if self.ListaTokens[self.i].tipo=="Claves":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo == 'Registro' :
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()        
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="imprimirln":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="imprimir":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="conteo":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="promedio":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="contarsi":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="datos":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="sumar":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="max":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="min":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="reporte":
            ins=self.instruccion()
            lista=self.Lista_Instrucciones2()
            return InstruccionListaInstrucciones(ins,lista)
        elif self.ListaTokens[self.i].tipo=="EOF":
            print("Analisis Sintactico exitoso")
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
            arbol.ejecutar({})
            arbol.getNodos()
            c=cadenas()
            cadena=c.Getearxd()
            print(cadena)
        else:
            cadena="¡¡¡ERROR SINTACTICO!!!\n"+self.listaErrores[0].descripcion+" en linea "+ str(self.listaErrores[0].linea)+" columna "+str(self.listaErrores[0].columna)
        return cadena
