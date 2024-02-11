from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class MyGUIFramework:
    def __init__(self):
        self.app = QApplication([])

    def create_window(self, title, width, height):
        window = QWidget()
        window.setWindowTitle(title)
        window.resize(width, height)
        return window

    def create_button(self, text, callback=None):
        button = QPushButton(text)
        if callback:
            button.clicked.connect(callback)
        return button

    def create_label(self, text):
        label = QLabel(text)
        return label

    def run(self):
        self.app.exec_()
