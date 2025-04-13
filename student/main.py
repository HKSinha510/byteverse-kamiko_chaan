import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from student.student_ui2 import Ui_MainWindow
from dbms.mongo import MongoConnection
from datetime import datetime
import json

class StudentDash(QMainWindow):
    def __init__(self, username=None):
        super(StudentDash, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect the send button to the send message function
        self.ui.Sendbutton.clicked.connect(self.send_message)
        self.ui.messagebox.returnPressed.connect(self.send_message)
        
        # Get username from login or from stored current user
        if username:
            self.username = username
        else:
            try:
                with open("dbms/currentuser.json", 'r') as f:
                    user_data = json.load(f)
                    self.username = user_data.get("username", "USER NAME")
            except:
                self.username = "USER NAME"

        # Update the username display in header
        self.ui.USERNAME.setHtml(f'''<!DOCTYPE HTML>
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p {{ white-space: pre-wrap; }}
</style></head><body>
<p style="margin: 0px;"><span style="font-size:16pt; font-style:italic;">{self.username}</span></p>
</body></html>''')

        # Set window title
        self.setWindowTitle("Student Dashboard")

        # Use the shared MongoDB connection
        self.mongo = MongoConnection("mydb")
        self.messages_collection = self.mongo.db["messages"]

        # Load old messages
        self.load_old_messages()

    def send_message(self):
        # Get the message text from QLineEdit
        message_text = self.ui.messagebox.text()
        
        if message_text.strip():  # Check if message is not empty
            # Format message with username
            formatted_message = f"{self.username}: {message_text}"
            
            # Add to message display using QListWidget
            self.ui.messagedisplay.addItem(formatted_message)
            
            # Clear the input box
            self.ui.messagebox.clear()
            
            # Send to server
            self.send_to_server(message_text)

    def send_to_server(self, message):
        message_doc = {
            "username": self.username,
            "message": message,
            "timestamp": datetime.now()
        }
        self.messages_collection.insert_one(message_doc)

    def load_old_messages(self):
        # Load previous messages, sorted by timestamp
        previous_messages = self.messages_collection.find().sort("timestamp", 1)

        for msg in previous_messages:
            formatted = f"{msg['username']}: {msg['message']}"
            self.ui.messagedisplay.addItem(formatted)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = StudentDash()
    widget.show()
    sys.exit(app.exec())