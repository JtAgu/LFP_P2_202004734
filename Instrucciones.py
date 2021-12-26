from Expresiones import*
from objeto import Objetos
import copy
import webbrowser

nombre=""
Pres=[]
Cursos=[]
Datos=[]
cadena=''
i=0

class InstruccionNombrandoRed():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global nombre
        global cadena
        valor= self.expresion.getValor(entorno)
        nombre=valor
        cadena+=" ************************"+valor+'************************\n\n'
        

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_NOMBRANDO_RED')

        idClav=str(Inicio())
        dot.node(idClav,'nombre_de_red')
        

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
        global Cursos
        valor= self.expresion.getValor(entorno)
        print(valor)
        cadena+=valor+'\n\n'
        for x in Cursos:
            for y in x.Pre:
                print(y)
            print("=====")
        

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


class InstruccionPorNombre():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global Cursos
        Encontrado=False
        valor= self.expresion.getValor(entorno)
        print(valor)
        for x in Cursos:
            if x.Nombre==valor:
                Encontrado==True
                cadena+="BUSCANDO POR NOMBRE ("+valor+")....\n************************\nCurso:\t"+x.Nombre+"\nSemestre:\t"+x.Semestre
                cadena+="\nCodigo:\t"+x.Codigo+"\nPrerrequisitos:\t["
                for y in x.Pre:
                    cadena+=y+","
                cadena+="]\n************************\n\n\n"
                break
        if Encontrado==False:
            cadena+="BUSCANDO POR NOMBRE ("+valor+")....\n***************************\nNO HAY RESULTADOS PARA LA BUSQUEDA\n***************************\n\n\n"


    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_BUSCAR_CURSO_NOMBRE')

        idClav=str(Inicio())
        dot.node(idClav,'cursoPorNombre')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        
        hijo= self.expresion.getNodos()
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
        dot.edge(idnodo,idPC)
        

        return idnodo


class InstruccionPorCodigo():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global Cursos
        Encontrado=False
        valor= self.expresion.getValor(entorno)
        print(valor)
        for x in Cursos:
            if x.Codigo==valor:
                Encontrado=True
                cadena+="BUSCANDO POR CODIGO ("+valor+")....\n************************\nCurso:\t"+x.Nombre+"\nSemestre:\t"+x.Semestre
                cadena+="\nCodigo:\t"+x.Codigo+"\nPrerrequisitos:\t["
                for y in x.Pre:
                    cadena+=y+","
                cadena+="]\n************************\n\n\n"
                break
        if Encontrado==False:
            cadena+="BUSCANDO POR CODIGO ("+valor+")....\n***************************\nNO HAY RESULTADOS PARA LA BUSQUEDA\n***************************\n\n\n"

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_BUSCAR_CURSO_CODIGO')

        idClav=str(Inicio())
        dot.node(idClav,'cursoPorCodigo')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        
        hijo= self.expresion.getNodos()
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
        dot.edge(idnodo,idPC)
        

        return idnodo

   
class InstruccionPorSemestre():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global Cursos
        Encontrado=False
        valor= self.expresion.getValor(entorno)
        print(valor)
        cadena+="BUSCANDO POR SEMESTRE ("+valor+")....\n****************************\n"
        for x in Cursos:
            if x.Semestre==valor:
                Encontrado=True
                cadena+="\nCurso:\t"+x.Nombre+"\nSemestre:\t"+x.Semestre
                cadena+="\nCodigo:\t"+x.Codigo+"\nPrerrequisitos:\t["
                for y in x.Pre:
                    cadena+=y+","
                cadena+="]\n"
        
        if Encontrado==False:
            cadena+="NO HAY RESULTADOS PARA LA BUSQUEDA"
        cadena+="\n****************************\n\n\n"

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_BUSCAR_CURSO_SEMESTRE')

        idClav=str(Inicio())
        dot.node(idClav,'cursoPorSemestre')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        
        hijo= self.expresion.getNodos()
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
        dot.edge(idnodo,idPC)
        

        return idnodo


class InstruccionPorPostRequisito():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global Cursos
        Encontrado=False
        valor= self.expresion.getValor(entorno)
        print(valor)
        cadena+="BUSCANDO POSTRREQUISITOS DE ("+valor+")....\n****************************\n"
        for x in Cursos:
            if x.Codigo==valor:
                Encontrado=True
                cadena+="Curso:"+x.Nombre+"\nPostrrequisitos:\n"
                break

        for x in Cursos:
            for y in x.Pre:
                if y==valor:
                    cadena+="\t"+x.Nombre+"\n"

        if Encontrado==False:
            cadena+="NO HAY RESULTADOS PARA LA BUSQUEDA"
        cadena+="\n****************************\n\n\n"

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_BUSCAR_POSTRREQUISITOS_CURSO')

        idClav=str(Inicio())
        dot.node(idClav,'cursoPostrrequisitos')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        
        hijo= self.expresion.getNodos()
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
        dot.edge(idnodo,idPC)
        

        return idnodo


class InstruccionPorPreRequisito():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global Cursos
        Encontrado=False
        valor= self.expresion.getValor(entorno)
        PreActual=[]
        print(valor)
        cadena+="BUSCANDO PRERREQUISITOS DE ("+valor+")....\n****************************\n"
        for x in Cursos:
            if x.Codigo==valor:
                Encontrado=True
                cadena+="Curso:"+x.Nombre+"\nPrerrequisitos:\n"
                for y in x.Pre:
                    PreActual.append(y)
                break

        
        for x in PreActual:
            for y in Cursos:
                if y.Codigo==x:
                    cadena+="\t"+y.Nombre+"\n"
                    break

        if Encontrado==False:
            cadena+="NO HAY RESULTADOS PARA LA BUSQUEDA"
        cadena+="\n****************************\n\n\n"

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_BUSCAR_PRERREQUISITOS_CURSO')

        idClav=str(Inicio())
        dot.node(idClav,'cursosPrerrequisitos')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        
        hijo= self.expresion.getNodos()
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
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
        dot.node(idnodo,"LISTA_VAL_PRE")
        if self.expresion:

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:
                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)
        return idnodo

class InstruccionListaValRegistros2():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global i
        i+=1
        if self.instruccion:
            if i<=3:
                r=self.instruccion.getValor(entorno)
                Datos.append(r)
                if self.lista:
                    self.lista.ejecutar(entorno)
            else:
                i=0
                self.instruccion.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_CURSO2")
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
        global i
        i+=1
        if self.expresion:
            r=self.expresion.getValor(entorno)
            Datos.append(r) 
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_VAL_CURSO")
        if self.expresion:

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionRegistro():
    
    def __init__(self,instruccion):
        
        self.instruccion=instruccion
    
    def ejecutar(self,entorno):
        global Cursos
        self.instruccion.ejecutar(entorno)
        self.Armar(Cursos)
        

    def Armar(self,lista):
        global Cursos
        global Pres
        global Datos
        Semestre=Datos[0]
        Cod=Datos[1]
        Nom=Datos[2]
        Curso=Objetos(Semestre,Cod,Nom)
        for x in Pres:
            Curso.Pre.append(x)
        Cursos.append(Curso)
        Pres.clear()
        Datos.clear()
        
        

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CREAR_CURSO')

        idClav=str(Inicio())
        dot.node(idClav,'crearcurso')
        

        idParA=str(Inicio())
        dot.node(idParA,'(')
        

        hijo= self.instruccion.getNodos()
        
        
        idParC=str(Inicio())
        dot.node(idParC,')')

        idPunCom=str(Inicio())
        dot.node(idPunCom,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idParA)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idParC)
        dot.edge(idnodo,idPunCom)
        

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