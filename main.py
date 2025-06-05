
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

#Create Class for Calculator App
class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        

        #set two lineEdits for both number inputs
        Input1 = QLineEdit(self)
        Input2 = QLineEdit(self)
        #Label for showing result
        Result = QLabel(self)
        #PushButtons for our math operations
        Plus = QPushButton("+")
        minus = QPushButton("-")
        multiply = QPushButton("x")
        divide = QPushButton("÷")
        #LayoutCreation 
        VLayout = QVBoxLayout()
        HLayout = QHBoxLayout()
        VLayout.addWidget(Input1)
        VLayout.addWidget(Input2)
        HLayout.addWidget(Plus)
        HLayout.addWidget(minus)
        HLayout.addWidget(multiply)
        HLayout.addWidget(divide)
        VLayout.addLayout(HLayout)
        VLayout.addWidget(Result)

        #apply layout
        self.setLayout(VLayout)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    app.exec()