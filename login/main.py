import sys
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog  # Import the UI class we generated

class LoginForm(QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Login Form")
        
        # Connect the login button to a function
        self.ui.loginbutton.clicked.connect(self.login)
        
        # Setup password input to show dots instead of characters
        self.ui.password_input.setEchoMode(self.ui.password_input.EchoMode.Password)
        
    def login(self):
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()


        QMessageBox.information(self, "Success", "Login successful!")
            
            # Close the login window
        self.accept()
        """
        # Add your authentication logic here
        # This is a simple example - you'd typically check against a database
        if email == "admin@example.com" and password == "password123":
            QMessageBox.information(self, "Login Successful", "Welcome!")
            # Here you could close this dialog and open your main application
            # self.accept()  # This will close the dialog with an "accept" result
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password!")"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginForm()
    widget.show()
    sys.exit(app.exec())