from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Window1(QMainWindow):
    size = 0

    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle("Viktoriin")
        self.setGeometry(0, 0, 1000, 500)
        self.init_layout()

    def init_layout(self):
        self.setStyleSheet("background-color: #282B30;")

        main_layout = QHBoxLayout()

        left_side_layout = QVBoxLayout()
        right_side_layout = QVBoxLayout()

        self.text_box_question = QLineEdit(self)
        self.text_box_question.setPlaceholderText("Question")
        self.text_box_question.setFont(QFont("Arial", 16))
        self.text_box_question.setStyleSheet("border: 5px solid; border-color: #00FFF6; color: #00FFF6;")
        self.text_box_question.setMaximumWidth(500)

        self.rb1 = QRadioButton("Single-choice")
        self.rb1.setStyleSheet("color: white")
        self.rb1.setFont(QFont('Arial', 12))

        self.rb2 = QRadioButton("Multiple choice")
        self.rb2.setStyleSheet("color: white")
        self.rb2.setFont(QFont('Arial', 12))

        self.rb3 = QRadioButton("Open-answer")
        self.rb3.setStyleSheet("color: white")
        self.rb3.setFont(QFont('Arial', 12))

        self.text_box_option = QLineEdit(self)
        self.text_box_option.setFont(QFont("Arial", 16))
        self.text_box_option.setStyleSheet("border: 2px solid; border-color: #00FFF6; color: #00FFF6;")
        self.text_box_option.setMaximumWidth(500)

        self.button_addoption = QPushButton("Add option")
        self.button_addoption.setFont(QFont('', 12))
        self.button_addoption.setStyleSheet("border: 2px solid; border-color: #00FFF6; color: #00FFF6;")
        self.button_addoption.setMaximumWidth(300)
        self.button_addoption.clicked.connect(self.add_option)

        self.button_register_question = QPushButton("Register Question")
        self.button_register_question.setFont(QFont('', 12))
        self.button_register_question.setStyleSheet("border: 2px solid; border-color: #00FFF6; color: #00FFF6;")
        self.button_register_question.setMaximumWidth(300)
        self.button_register_question.clicked.connect(self.register_question)

        left_side_layout.addWidget(self.text_box_question)
        left_side_layout.addWidget(self.rb1)
        left_side_layout.addWidget(self.rb2)
        left_side_layout.addWidget(self.rb3)
        left_side_layout.addWidget(self.text_box_option)
        left_side_layout.addWidget(self.button_addoption)
        left_side_layout.addWidget(self.button_register_question)

        label1 = QLabel("Questions")
        label1.setStyleSheet("color: #00FFF6;")
        label1.setFont(QFont("Arial" , 15 ))
        right_side_layout.addWidget(label1, alignment=Qt.AlignTop | Qt.AlignRight)

        self.question_label = QLabel("")
        self.question_label.setStyleSheet("color: #00FFF6;")

        self.button_continue = QPushButton("Continue")
        self.button_continue.setFont(QFont("Arial" , 12))
        self.button_continue.setStyleSheet("border: 2px solid; border-color: #00FFF6; color: #00FFF6;")
        right_side_layout.addWidget(self.question_label, alignment=Qt.AlignTop | Qt.AlignRight)
        right_side_layout.addWidget(self.button_continue)

        main_layout.addLayout(left_side_layout)
        main_layout.addLayout(right_side_layout)
        left_side_layout.addStretch()

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def register_question(self):
        question_text = self.question_label.text()
        new_question = self.text_box_question.text()
        if question_text:
            question_text += '\n' + new_question
        else:
            question_text = new_question
        self.question_label.setText(question_text)

    def add_option(self):
        option_text = self.text_box_option.text()
        current_text = self.question_label.text()

        if current_text:
            current_text += f'\n- {option_text}'
        else:
            current_text = f'- {option_text}'

        self.question_label.setText(current_text)
        self.text_box_option.clear()

app = QApplication(sys.argv)
screen = Window1()
screen.show()
sys.exit(app.exec_())
