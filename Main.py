# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
import copy
import webbrowser
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.Ruta=""
        self.scanner = AnalizadorLexico()
        self.Sintactico = AnalizadorSintactico()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CodigoArea = QtWidgets.QTextEdit(self.centralwidget)
        self.CodigoArea.setGeometry(QtCore.QRect(15, 50, 451, 501))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        self.CodigoArea.setFont(font)
        self.CodigoArea.setObjectName("CodigoArea")
        self.ConsolaArea = QtWidgets.QTextEdit(self.centralwidget)
        self.ConsolaArea.setGeometry(QtCore.QRect(480, 50, 501, 501))
        self.ConsolaArea.setObjectName("ConsolaArea")
        self.BTN_Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Cargar.setGeometry(QtCore.QRect(350, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.BTN_Cargar.setFont(font)
        self.BTN_Cargar.setObjectName("BTN_Cargar")
        self.BTN_Reportar = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Reportar.setGeometry(QtCore.QRect(830, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.BTN_Reportar.setFont(font)
        self.BTN_Reportar.setObjectName("BTN_Reportar")
        self.BTN_Analizar = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Analizar.setGeometry(QtCore.QRect(510, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.BTN_Analizar.setFont(font)
        self.BTN_Analizar.setObjectName("BTN_Analizar")
        self.CmbReporte = QtWidgets.QComboBox(self.centralwidget)
        self.CmbReporte.setGeometry(QtCore.QRect(670, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.CmbReporte.setFont(font)
        self.CmbReporte.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmbReporte.setObjectName("CmbReporte")
        self.CmbReporte.addItem("")
        self.CmbReporte.addItem("")
        self.CmbReporte.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.BTN_Cargar.clicked.connect(self.FuncionCargar)
        self.BTN_Reportar.clicked.connect(self.Reportes)
        self.BTN_Analizar.clicked.connect(self.Analizar)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "[LFP]Proyecto2"))
        self.BTN_Cargar.setText(_translate("MainWindow", "CARGAR"))
        self.BTN_Reportar.setText(_translate("MainWindow", "REPORTAR"))
        self.BTN_Analizar.setText(_translate("MainWindow", "ANALIZAR"))
        self.CmbReporte.setItemText(0, _translate("MainWindow", "ERRORES"))
        self.CmbReporte.setItemText(1, _translate("MainWindow", "TOKENS"))
        self.CmbReporte.setItemText(2, _translate("MainWindow", "DERIVACION"))
        self.BTN_Analizar.setDisabled(True)
        self.BTN_Reportar.setDisabled(True)

    def Analizar(self):
        self.scanner.listaErrores=[]
        self.scanner.listaTokens=[]
        self.Sintactico.listaErrores=[]
        self.Sintactico.ListaTokens=[]
        contenido=self.CodigoArea.toPlainText()
        self.scanner.analizar(contenido)
        self.scanner.impTokens()
        print("======================================================================")
        print("======================================================================")
        self.scanner.impErrores()
        cadena=self.Sintactico.analizar(self.scanner.listaTokens)
        self.Sintactico.ImpErrores()
        self.ConsolaArea.setText(cadena)
        self.BTN_Reportar.setDisabled(False)
        

    def FuncionCargar(self):
        buscar = QFileDialog.getOpenFileName()
        self.Ruta=buscar[0]
        size=len(buscar[0])
        final=""
        for x in buscar[0]:
            if size<5:
                final+=x
            size-=1
        if final==".lfp":
            codigo_fuente = open(buscar[0], 'r')
            contenido = codigo_fuente.read()
            codigo_fuente.close()
            self.CodigoArea.setText(contenido)
            self.BTN_Analizar.setDisabled(False)
        else:
            msg=QMessageBox()
            msg.setWindowTitle("OCURRIO UN ERROR")
            msg.setText("Extension de archivo incorrecta")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()
        

    def Reportes(self):
        Reporte=self.CmbReporte.currentText()
        contenido=""
        if Reporte=="ERRORES":
            c=0
            file=open('Errores.html','w')
            contenido="""<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
            <title>REPORTE ERRORES</title>
            </head>
            <body><center><h1>REPORTE DE ERRORES</h1></center><br>
            <div WIDTH='700'>
            <table class='table table-striped table-hover'  border='1'style='margin-left:auto;margin-right:auto;margin-top:auto;'><tbody>
            <tr><th>Lexema</th><th>Tipo</th><th>Linea</th><th>Columna</th></tr>"""
            for x in self.scanner.listaErrores:
                contenido+='<tr><td>'+str(x.descripcion)+'</td>'
                contenido+='<td>'+str(x.tipo)+'</td>'
                contenido+='<td>'+str(x.linea)+'</td>'
                contenido+='<td>'+str(x.columna)+'</td></tr>'
            for x in self.Sintactico.listaErrores:
                contenido+='<tr><td>'+str(x.descripcion)+'</td>'
                contenido+='<td>'+str(x.tipo)+'</td>'
                contenido+='<td>'+str(x.linea)+'</td>'
                contenido+='<td>'+str(x.columna)+'</td></tr>'
            contenido+='</tbody></table>'
            contenido+='</body></div></html>'
            try:
                file.write(contenido)
            except:
                print("Ocurrio un error")
            finally:
                file.close()
                webbrowser.open_new_tab('Errores.html')
        elif Reporte=="TOKENS":
            file=open('Tokens.html','w')
            c=0
            contenido="""<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>REPORTE</title>
            </head>
            <body>

            <center><h1>REPORTE DE TOKENS</h1></center><br>
            <div WIDTH='700'>
            <table class='table table-striped table-hover'  border='1'style='margin-left:auto;margin-right:auto;margin-top:auto;'><tbody>
            <tr><th>Lexema</th><th>Tipo</th><th>Linea</th><th>Columna</th></tr>"""
            for x in self.scanner.listaTokens:
                contenido+='<tr><td>'+str(x.lexema)+'</td>'
                contenido+='<td>'+str(x.tipo)+'</td>'
                contenido+='<td>'+str(x.linea)+'</td>'
                contenido+='<td>'+str(x.columna)+'</td></tr>'
            contenido+='</tbody></table>'
            contenido+='</body></div></html>'
            try:
                file.write(contenido)
            except:
                print("Ocurrio un error")
            finally:
                file.close()
                webbrowser.open_new_tab("Tokens.html")
        else:
            webbrowser.open_new_tab("arbol.gv.pdf")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
