from pyfirmata import Arduino, util
from PyQt5 import uic,QtWidgets
import time

#========== Conexão com Arduino ================================
Uno = Arduino('COM13') # Portas que está conectado o arduino
it = util.Iterator(Uno)
it.start()
#===========Configuração dos Pinos==============================
valD13 = Uno.get_pin('d:13:i')# Pino 13 é Input
valD12 = Uno.get_pin('d:12:i')# Pino 12 é Input
valD11 = Uno.get_pin('d:11:i')# Pino 11 é Input
#===========Configuração dos Pinos==============================
estadoBt1Ant = True #Estado HIGH - Ligado
estadoBt2Ant = True #Estado HIGH - Ligado
estadoBt3Ant = True #Estado HIGH - Ligado
#========== Conexão com Interface================================
app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
BtnCortar = interface.BtnCortar()
BtnParar = interface.BtnParar()
def cortar():
    Uno.digital[5].write(1)
    while True:
        time.sleep(0.15)
        btnCortar  = valD11.read()
        btnParar = valD12.read()
        btnCortar = BtnCortar
        if btnCortar == BtnCortar:
            interface.BtnCortar.clicked.connect(cortar)
