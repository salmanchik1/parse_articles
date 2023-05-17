import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect a button click event to a function
        self.ui.selectFolderPushButton.clicked.connect(self.show_message_box)

    def show_select_folder_dialog(self):
        self.root_path = QFileDialog.getExistingDirectory(
            self, "Select Folder", options=QFileDialog.ShowDirsOnly)
        if self.root_path:
            print("Selected folder:", self.root_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
