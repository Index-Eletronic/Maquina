from pyfirmata import Arduino, util
from PyQt5 import uic,QtWidgets
import time

#========== Conexão com Arduino ================================
Uno = Arduino('COM1') # Portas que está conectado o arduino
it = util.Iterator(Uno)
it.start()
#===========Configuração dos Pinos==============================
valD13 = Uno.get_pin('d:13:i')# Pino 13 é Input controladas por botão/sensor (d = digital, numero da porta, input  = pinMode
valD12 = Uno.get_pin('d:12:i')# Pino 12 é Input
valD11 = ('interface.ui[BtnCortar]')# Pino 11 é Input
#===========Configuração dos Pinos==============================
#estadoBt1Ant = True #Variavel que detecta o estado do botão
#estadoBt2Ant = True #Variavel que detecta o estado do botão
#estadoBt3Ant = True #Variavel que detecta o estado do botão
#========== Conexão com Interface================================

while True: # = Void Loop()
    time.sleep(0.15)
    def funcao_principal():
        if valD11 == True:
            Uno.digital[13].write(1)
            print('LED ARDUINO ACENDEU')
        else:
            Uno.digital[13].write(0)
    break

app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
interface.BtnCortar.clicked.connect(funcao_principal)

interface.show()
app.exec()