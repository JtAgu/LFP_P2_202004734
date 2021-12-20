from Expresiones import*
from objeto import Objetos
import copy
import webbrowser

Pres=[]
Cursos=[]
Objeto=[]
cadena=''


class InstruccionImprimir():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        valor= self.expresion.getValor(entorno)
        print(valor,end='')
        cadena+=valor


    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CONSOLA')

        idClav=str(Inicio())
        dot.node(idClav,'consola')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'(')
        
        hijo= self.expresion.getNodos()

        idCorC=str(Inicio())
        dot.node(idCorC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idCorC)
        dot.edge(idnodo,idPC)
        

        return idnodo
        
class InstruccionImprimirLn():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        valor= self.expresion.getValor(entorno)
        print(valor)
        cadena+=valor+'\n'

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CONSOLALN')

        idClav=str(Inicio())
        dot.node(idClav,'consolaln')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'(')
        
        hijo= self.expresion.getNodos()
        
        idCorC=str(Inicio())
        dot.node(idCorC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idCorC)
        dot.edge(idnodo,idPC)
        

        return idnodo


class InstruccionContarSi():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global cadena
        val= self.expresion.getValor(entorno)
        valor=val.split(',')
        c=0
        l=[]
        for x in Objeto:
            if str(x.Clave)==str(valor[0]):
                l=x.Listas
        
        for x in l:
            if str(x)==str(valor[1]):
                c+=1
        print("\n>>> "+str(c))
        cadena+="\n>>> "+str(c)


    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CONTARSI')

        idClav=str(Inicio())
        dot.node(idClav,'contarsi')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'(')
        

        hijo= self.expresion.getNodos()
        
        
        idCorC=str(Inicio())
        dot.node(idCorC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idCorC)
        dot.edge(idnodo,idPC)
        

        return idnodo
        


class InstruccionListaVaLPre2():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global Pres
        if self.instruccion:
            r=self.instruccion.getValor(entorno)
            Pres.append(r)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_PRE2")
        if self.instruccion:
            
            idComa=str(Inicio())
            dot.node(idComa,',')
            dot.edge(idnodo,idComa)

            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionListaValPre():
    def __init__(self,instruccion,lista):
        self.expresion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global registros
        if self.expresion:
            r=self.expresion.getValor(entorno)
            Pres.append(r) 
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_REG")
        if self.expresion:

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

    def __init__(self,instruccion,lista):
        self.expresion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        if self.expresion:
            self.expresion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_REGISTROS")
        if self.expresion:
            idLlaveA=str(Inicio())
            dot.node(idLlaveA,'{')
            dot.edge(idnodo,idLlaveA)

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            idLlaveC=str(Inicio())
            dot.node(idLlaveC,'}')
            dot.edge(idnodo,idLlaveC)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionListaValRegistros2():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global registros
        if self.instruccion:
            r=self.instruccion.getValor(entorno)
            registros.append(r)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_REG2")
        if self.instruccion:
            
            idComa=str(Inicio())
            dot.node(idComa,',')
            dot.edge(idnodo,idComa)

            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionListaValRegistros():
    def __init__(self,instruccion,lista):
        self.expresion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global registros
        if self.expresion:
            r=self.expresion.getValor(entorno)
            registros.append(r) 
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_REG")
        if self.expresion:

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

    def __init__(self,instruccion,lista):
        self.expresion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        if self.expresion:
            self.expresion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_REGISTROS")
        if self.expresion:
            idLlaveA=str(Inicio())
            dot.node(idLlaveA,'{')
            dot.edge(idnodo,idLlaveA)

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            idLlaveC=str(Inicio())
            dot.node(idLlaveC,'}')
            dot.edge(idnodo,idLlaveC)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionRegistro():
    def __init__(self,instruccion):
        
        self.instruccion=instruccion
    
    def ejecutar(self,entorno):
        global cadena
        global Objeto
        self.instruccion.ejecutar(entorno)
        
        

    def Armar(self,lista):
        
        global Objeto
        c=0
        c2=0
        while c < len(lista):
            if c2<len(Objeto):
                Objeto[c2].Listas.append(lista[c])
                c2+=1
                c+=1
            else:
                c2=0

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_REGISTRO')

        idClav=str(Inicio())
        dot.node(idClav,'Registro')
        

        idigual=str(Inicio())
        dot.node(idigual,'=')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'[')
        

        hijo= self.instruccion.getNodos()
        
        
        idCorC=str(Inicio())
        dot.node(idCorC,']')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idigual)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idCorC)
        

        return idnodo



class InstruccionInstruccion():
    def __init__(self,instruccion):
        self.instruccion=instruccion
    
    def ejecutar(self,entorno):
        self.instruccion.ejecutar(entorno)
    
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INSTRUCCION')

        hijo= self.instruccion.getNodos()

        dot.edge(idnodo,hijo)

        return idnodo

class InstruccionListaInstrucciones2():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_INSTRUCCIONES2")
        if self.instruccion:
            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)
            if self.lista:
                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)
        return idnodo

class InstruccionListaInstrucciones():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_INSTRUCCIONES")
        if self.instruccion:
            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)
            if self.lista:
                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)
        return idnodo
    
class InstruccionInicio():
    def __init__(self,lista):
        self.lista=lista
    
    def ejecutar(self,entorno):
        self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INICIO')

        hijo= self.lista.getNodos()

        dot.edge(idnodo,hijo)
        dot.view()

        return idnodo

class cadenas():
    def __init__(self):
        global cadena
        self.valor=cadena
    
    def Getearxd(self):
        global cadena
        print (cadena)
        return cadena
        
class InstruccionEpsilon():
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

    def getNodos(self):
        global dot

        idnodo = str(Inicio())
        dot.node(idnodo, '$')
        
        return idnodo