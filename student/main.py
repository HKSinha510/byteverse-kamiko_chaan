import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from student.student_ui import Ui_MainWindow

class StudentDash(QMainWindow):  # Change from QDialog to QMainWindow
    def __init__(self):
        super(StudentDash, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Student Dashboard")        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = StudentDash()
    widget.show()
    sys.exit(app.exec())