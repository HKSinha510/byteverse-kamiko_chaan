#Kamiko_chaan
#todo:
#1. add forget password button
#2. enable register button
#3. add border if any field is empty

import os, sys, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog  # Import the UI class we generated
from student.main import StudentDash
from teacher.main import TeacherDash

from dbms.mongo import MongoConnection

con = MongoConnection("mydb")
users = con.get_collection("users")


class LoginForm(QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Login")
        
        # Connect the login button to a function
        self.ui.login_next.clicked.connect(self.login)
        self.ui.register_2.clicked.connect(self.register)
        
        # Setup password input to show dots instead of characters
        self.ui.password_input.setEchoMode(self.ui.password_input.EchoMode.Password)
        
    def login(self):
        user = self.ui.user_input.text()
        password = self.ui.password_input.text()

        if user == "" and password == "":
            pass
        
        else: 
            if user == "":
                QMessageBox.warning(self, "User not Found", "Please enter Username")
            if password == "":
                QMessageBox.warning(self, "Invalid Password", "Please enter Password")

            if user != "" and password != "":
                d = users.find_one({"username": user})
                if d == None:
                    QMessageBox.warning(self, "User not found", "user not found")

                else:
                    if password == d["password"]:
                        QMessageBox.information(self, "Successful", "Login Successful!")
                        self.accept()

                        ## save current user 
                        with open("dbms/currentuser.json", 'w') as f:
                            d.pop('_id', None)
                            json.dump(d, f, indent=4)

                        ##
                        
                        if user.startswith("S"):
                            self.dashboard = StudentDash(user)  # Pass username to StudentDash
                        elif user.startswith("T"):
                            self.dashboard = TeacherDash()

                        self.dashboard.show()

                    else:
                        QMessageBox.warning(self, "Incorrect Password", "Incorrect Password")
        
    def register(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginForm()
    widget.show()
    sys.exit(app.exec())