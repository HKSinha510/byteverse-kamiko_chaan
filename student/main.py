import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from student.student_ui2 import Ui_MainWindow

from dbms.mongo import MongoConnection
from datetime import datetime

class StudentDash(QMainWindow):  # Change from QDialog to QMainWindow
    def __init__(self):
        super(StudentDash, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Connect the send button to the sen message function
        self.ui.Sendbutton.clicked.connect(self.send_message)
        self.ui.messagebox.returnPressed.connect(self.send_message)
        
        # Store username for display with messages
        self.username = "USER NAME"  # Replace with actual user login system later

        # Set window title
        self.setWindowTitle("Student Dashboard")

        # Use the shared MongoDB connection
        self.mongo = MongoConnection("mydb")
        self.messages_collection = self.mongo.db["messages"]

        #Load old messages
        self.load_old_messages()

    def send_message(self):
    # Get the message text

        message_text = self.ui.messagebox.toPlainText()  # For QTextEdit
        
        if message_text.strip():  #Check if message is not empty
            # Format message with username (simple version)
            formatted_message = f"{self.username}: {message_text}"
            
            # Add to message display
            self.ui.messageDisplay.append(formatted_message)  # For QTextBrowser
            # OR
            # self.ui.messageDisplay.addItem(formatted_message)  # For QListWidget
            
            # Clear the input box
            self.ui.messagebox.clear()
            
            # Send to server (covered in network section)
            self.send_to_server(message_text)

    def send_to_server(self, message):
        message_doc = {
            "username": self.username,
            "message": message,
            "timestamp": datetime.datetime.now(datetime.timezone.utc)
        }
        self.messages_collection.insert_one(message_doc)

    def load_old_messages(self):
        # Load previous messages, sorted by timestamp
        previous_messages = self.messages_collection.find().sort("timestamp", 1)

        for msg in previous_messages:
            formatted = f"{msg['username']}: {msg['message']}"
            self.ui.messageDisplay.append(formatted)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = StudentDash()
    widget.show()
    sys.exit(app.exec())