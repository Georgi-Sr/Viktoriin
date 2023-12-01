from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
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
        self.setStyleSheet("background-color: #282B30;")
        
        self.setWindowTitle("Determinant")

        self.setStyleSheet("background-color: #121212;")

        self.main_layout = QVBoxLayout()


        
        text_box = QLineEdit(self)
        text_box.setPlaceholderText("Question")
        text_box.setFont(QFont("Arial" , 16 ))
        text_box.setStyleSheet("border :5px solid ;" "border-color : #00FFF6;; color: #00FFF6;;")


        self.rb1 = QRadioButton("single-choice")
        self.rb1.setStyleSheet("color : white")
        self.rb1.setFont(QFont('Arial' , 12))
        self.rb2 = QRadioButton("multiple choice")
        self.rb2.setStyleSheet("color : white")
        self.rb2.setFont(QFont('Arial' , 12))
        self.rb3 = QRadioButton("open-answer")
        self.rb3.setStyleSheet("color : white")
        self.rb3.setFont(QFont('Arial' , 12))
        
        layout_1 = QVBoxLayout()
        layout_1.addWidget(text_box)

        layout_2 = QVBoxLayout()
        layout_2.addWidget(self.rb1)
        layout_2.addWidget(self.rb2)
        layout_2.addWidget(self.rb3)
        layout_2.addStretch()
        
        text_box = QLineEdit(self)
        text_box.setFont(QFont("Arial" , 16 ))
        text_box.setStyleSheet("border :2px solid ;" "border-color : #00FFF6;; color: #00FFF6;;")

        layout_3 = QVBoxLayout()
        layout_3.addWidget(text_box)
        layout_3.addStretch()

        self.button = QPushButton("Add option")
        self.button.setFont(QFont('' , 20))
        self.button.setStyleSheet("border :2px solid ;" "border-color : #00FFF6;; color: #00FFF6;;")
        
        layout_4 = QHBoxLayout()
        layout_4.addStretch()
        layout_4.addWidget(self.button)

        
        


        widget = QWidget(self)
        central_layout = QVBoxLayout()
        central_layout.addLayout(layout_1)
        central_layout.addLayout(layout_2)
        central_layout.addLayout(layout_3)
        central_layout.addLayout(layout_4)
        widget.setLayout(central_layout)
        self.setCentralWidget(widget)











app = QApplication(sys.argv)
screen = Window1()
screen.show()
sys.exit(app.exec_())
