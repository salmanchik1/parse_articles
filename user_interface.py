from MainWindow_ui import Ui_MainWindow


class Ui_MainWindow_mod(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def root_path(self):
        return self.rootPathlineEdit.text()

    @root_path.setter
    def root_path(self, value):
        self.rootPathlineEdit.setText(value)
