from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
QRadioButton, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
import sys

class Window1(QMainWindow):
    size = 0

    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle("Viktoriin")
        self.setGeometry(0, 0, 400, 500)
        self.init_layout()
  
    def init_layout(self):
        self.setWindowTitle("Viktoriin")
        self.setStyleSheet("background-color: #282B30;")
        self.main_layout = QVBoxLayout()
        self.layout_1 = QHBoxLayout()

        self.button = QPushButton("Create Test")
        self.button.setFont(QFont('' , 20))
        self.button.setStyleSheet("border :5px solid ;" "border-color : #00FFF6;; color: #00FFF6;;")
        self.main_layout.addWidget(self.button)
        self.main_layout.addLayout(self.layout_1)
        
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
        self.setCentralWidget(widget)
    
    
app = QApplication(sys.argv)
screen = Window1()
screen.show()
sys.exit(app.exec_())

        
