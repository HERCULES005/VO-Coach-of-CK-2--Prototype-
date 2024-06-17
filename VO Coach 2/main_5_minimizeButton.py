import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class MinimizedWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(50, 50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(150, 0, 150, 200))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.rect())

    def mousePressEvent(self, event):
        self.parent().restore_main_window()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Custom Minimize Example')

        minimize_button = QPushButton('Minimize to Widget', self)
        minimize_button.clicked.connect(self.minimize_to_widget)
        minimize_button.resize(minimize_button.sizeHint())
        minimize_button.move(450, 50)

        self.minimized_widget = MinimizedWidget(self)
        self.minimized_widget.hide()

    def minimize_to_widget(self):
        self.hide()
        self.minimized_widget.move(self.frameGeometry().topLeft())
        self.minimized_widget.show()

    def restore_main_window(self):
        self.minimized_widget.hide()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
