from PyQt5 import uic, QtWidgets

def funcao_principal():
    print('teste')

app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
interface.BtnCortar.clicked.connect(funcao_principal)

interface.show()
app.exec()
