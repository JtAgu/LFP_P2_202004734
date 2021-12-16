from Expresiones import*
from objeto import Objetos
import copy
import webbrowser
clv=[]
registros=[]
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
        dot.node(idnodo,'INS_IMPRIMIR')

        idClav=str(Inicio())
        dot.node(idClav,'imprimir')
        

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
        dot.node(idnodo,'INS_IMPRIMIRLN')

        idClav=str(Inicio())
        dot.node(idClav,'imprimirln')
        

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

class InstruccionConteo():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global cadena
        global registros
        valor= self.expresion.getValor(entorno)
        print("\n>>> "+str(len(registros)))
        cadena+="\n>>> "+str(len(registros))+'\n'

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CONTAR')

        idClav=str(Inicio())
        dot.node(idClav,'conteo')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'(')
        
        
        idCorC=str(Inicio())
        dot.node(idCorC,')')

        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,idCorC)
        dot.edge(idnodo,idPC)
        

        return idnodo
    
    

class InstruccionReporte():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global Objeto
        valor= self.expresion.getValor(entorno)
        c=0
        file=open(valor+'.html','w')
        contenido="""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
            <title>REPORTE """+valor+"""</title>
            </head>
            <body><center><h1>"""+valor+"""</h1></center><br>
            <table class='table table-striped table-hover'  border='1'style='margin-left:auto;margin-right:auto;margin-top:auto;'><tbody>"""
        contenido+='<tr>'
        for x in Objeto:
            contenido+='<th>'+str(x.Clave)+'</th>'
        contenido+='<tr>'
        c1=0
        c2=0
        while c1<len(Objeto[0].Listas):
            contenido+='<tr>'
            while c2 < len(Objeto):
                contenido+='<td>'+str(Objeto[c2].Listas[c1])+'</td>'
                c2+=1            
            c1+=1
            c2=0
            contenido+='</tr>'

        contenido+='</tbody></table>'
        contenido+='</body></html>'
        try:
            file.write(contenido)
        except:
            print("Ocurrio un error")
        finally:
            file.close()
            webbrowser.open_new_tab(valor+'.html')

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_REPORTE')

        idClav=str(Inicio())
        dot.node(idClav,'exportarReporte')
        

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

class InstruccionMax():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global cadena
        valor= self.expresion.getValor(entorno)
        c=0
        l=[]
        for x in Objeto:
            if str(x.Clave)==str(valor):
                l=copy.copy(x.Listas)
        if len(l)>0:
            l.sort(reverse=True)
            print("\n>>> "+str(l[0]))
            cadena+="\n>>> "+str(l[0])+"\n"
        else:
            print("\n>>> Sin registros disponibles")
            cadena+="\n>>> Sin registros disponibles\n"
    
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_MAX')

        idClav=str(Inicio())
        dot.node(idClav,'max')
        

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

class InstruccionMin():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global cadena
        valor= self.expresion.getValor(entorno)
        c=0
        l=[]
        for x in Objeto:
            if str(x.Clave)==str(valor):
                l=copy.copy(x.Listas)
        if len(l)>0:
            l.sort()
            print("\n>>> "+str(l[0]))
            cadena+="\n>>> "+str(l[0])+"\n"
        else:
            print("\n>>> Sin registros disponibles")
            cadena+="\n>>> Sin registros disponibles\n"
        
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_MIN')

        idClav=str(Inicio())
        dot.node(idClav,'min')
        

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

class InstruccionSumar():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global cadena
        valor= self.expresion.getValor(entorno)
        c=0
        l=[]
        for x in Objeto:
            if str(x.Clave)==str(valor):
                l=x.Listas
        if len(l)>0:
            for x in l:
                c+=float(x)
            print("\n>>> "+str(c))
            cadena+="\n>>> "+str(c)+'\n'
        else:
            print("\n>>> Sin registros disponibles")
            cadena+="\n>>> Sin registros disponibles"+'\n'

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_SUMAR')

        idClav=str(Inicio())
        dot.node(idClav,'sumar')
        

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
                
class InstruccionDatos():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global Objeto
        global cadena
        valor= self.expresion.getValor(entorno)
        c='\n>>>'
        for x in Objeto:
            c+=x.Clave+'\t'
        c1=0
        c2=0
        while c1<len(Objeto[0].Listas):
            c+="\n>>> "
            while c2 < len(Objeto):
                c+=str(Objeto[c2].Listas[c1])+'\t'
                """if len(str(Objeto[c2].Listas[c1]))<8:
                    c+='\t'"""
                c2+=1            
            c1+=1
            c2=0
        cadena+=c+'\n'
        print(c)
    
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_DATOS')

        idClav=str(Inicio())
        dot.node(idClav,'datos')
        

        idCorA=str(Inicio())
        dot.node(idCorA,'(')
        
                
        idCorC=str(Inicio())
        dot.node(idCorC,')')
        
        idPC=str(Inicio())
        dot.node(idPC,';')

        dot.edge(idnodo,idClav)
        dot.edge(idnodo,idCorA)
        dot.edge(idnodo,idCorC)
        dot.edge(idnodo,idPC)
        

        return idnodo

        
class InstruccionPromedio():
    def __init__(self,expresion):
        self.expresion=expresion
    
    def ejecutar(self,entorno):
        global registros
        global Objeto   
        global cadena     
        valor= self.expresion.getValor(entorno)

        c=0
        l=[]
        for x in Objeto:
            if str(x.Clave)==str(valor):
                l=x.Listas
        if len(l)>0:
            for x in l:
                c+=float(x)
            c=c/len(l)
            c=round(c, 2)
            print("\n>>> "+str(c))
            cadena+="\n>>> "+str(c)+'\n'
        else:
            print("\n>>> Sin registros disponibles")
            cadena+="\n>>> Sin registros disponibles\n"
    
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_PROMEDIO')

        idClav=str(Inicio())
        dot.node(idClav,'promedio')
        

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
        


class InstruccionListaClaves2():
    def __init__(self,instruccion,lista):
        self.instruccion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        global clv
        if self.instruccion:
            c=self.instruccion.getValor(entorno)
            clv.append(c)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_CLAVES2")
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

class InstruccionListaClaves():
    def __init__(self,instruccion,lista):
        self.expresion=instruccion
        self.lista=lista
    
    def ejecutar(self,entorno):
        if self.expresion:
            c=self.expresion.getValor(entorno)
            clv.append(c)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,"LISTA_CLAVES")
        if self.expresion:

            hijo=self.expresion.getNodos()
            dot.edge(idnodo,hijo)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo

class InstruccionClave():
    def __init__(self,instruccion):
        
        self.instruccion=instruccion
    
    def ejecutar(self,entorno):
        global clv
        self.instruccion.ejecutar(entorno)
        for c in clv:
            nuevo=Objetos(c)
            Objeto.append(nuevo)

        
    def getNodos(self):
        global dot
        idnodo=str(Inicio())
        dot.node(idnodo,'INS_CLAVE')

        idClav=str(Inicio())
        dot.node(idClav,'Clave')
        

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

class InstruccionListaRegistros2():
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
        dot.node(idnodo,"LISTA_REGISTROS2")
        if self.instruccion:
            
            idLlaveA=str(Inicio())
            dot.node(idLlaveA,'{')
            dot.edge(idnodo,idLlaveA)

            hijo=self.instruccion.getNodos()
            dot.edge(idnodo,hijo)

            idLlaveC=str(Inicio())
            dot.node(idLlaveC,'}')
            dot.edge(idnodo,idLlaveC)

            if self.lista:

                hijo2=self.lista.getNodos()
                dot.edge(idnodo,hijo2)

        return idnodo
    
class InstruccionListaRegistros():
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
        global registros
        global clv
        global cadena
        global Objeto
        self.instruccion.ejecutar(entorno)
        
        self.Armar(registros)

    def Armar(self,lista):
        global registros
        global clv
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