from PyQt5 import uic, QtWidgets

'''
Calculo do micropassos para mm.
corte = 1000 * textbox lardura da fita
sensor = 1000 * texbox comprimento. - Numero de volta que o motor vai dar para cortar o comprimento solicitado.
'''

def funcao_principal():
    print('teste')
    '''
    digitalwrite (2, corte) - porta digita para tantomicro passos da largura da fita 
    sleep(10)
    analogWrite (5, HIGH) - POrta para ligar o corte.
    time (sensor)
    analogWrite (5, LOW ) - Desliga o motor. 
    '''

app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
interface.BtnCortar.clicked.connect(funcao_principal)

interface.show()
app.exec()
