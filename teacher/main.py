import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from teacher.teacher_ui import Ui_MainWindow

class TeacherDash(QMainWindow):  # Change from QDialog to QMainWindow
    def __init__(self):
        super(TeacherDash, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Teacher Dashboard")        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TeacherDash()
    widget.show()
    sys.exit(app.exec())