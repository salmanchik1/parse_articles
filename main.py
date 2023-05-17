import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui", self)  # Load the user interface file

        # Connect a button click event to a function
        self.pushButton.clicked.connect(self.show_message_box)

    def show_message_box(self):
        QMessageBox.information(self, "Message", "Hello, PyQt5!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
