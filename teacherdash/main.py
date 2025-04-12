import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from teacher import Ui_MainWindow  # Import the UI class we generated

class TeacherDash(QMainWindow):  # Change from QDialog to QMainWindow
    def __init__(self):
        super(TeacherDash, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Dashboard")        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TeacherDash()
    widget.show()
    sys.exit(app.exec())