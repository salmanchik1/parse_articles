import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from user_interface import Ui_MainWindow_mod as Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect a button click event to a function
        self.ui.selectFolderPushButton.clicked.connect(self.select_folder)

    def select_folder(self):
        root_path = QFileDialog.getExistingDirectory(
            self, "Select Folder", options=QFileDialog.ShowDirsOnly)
        if root_path:
            self.ui.root_path = root_path
            print("Selected folder:", root_path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
