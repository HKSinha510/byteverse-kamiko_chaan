
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QFrame
from PyQt6.QtGui import QPixmap, QFont, QColor
from PyQt6.QtCore import Qt, QRect
import sys

class KamikochaanWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kamikochaan")
        self.setGeometry(100, 100, 640, 360)
        self.setStyleSheet("background-color: #000019;")

        # Main widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Image (Top Left)
        self.image_label = QLabel(self.central_widget)
        self.image_label.setGeometry(22, 21, 102, 88)
        self.image_label.setPixmap(QPixmap("template_image.png").scaled(102, 88, Qt.AspectRatioMode.KeepAspectRatio))
        self.image_label.setStyleSheet("background-color: transparent;")

        # User name
        self.user_label = QLabel("USER NAME", self.central_widget)
        self.user_label.setGeometry(130, 49, 238, 32)
        self.user_label.setStyleSheet("color: #ffffff; font-family: Verdana;")
        self.user_label.setFont(QFont("Verdana", 16, weight=QFont.Weight.DemiBold, italic=True))

        # Institute name
        self.institute_label = QLabel("@Institute name", self.central_widget)
        self.institute_label.setGeometry(130, 77, 238, 32)
        self.institute_label.setStyleSheet("color: #c2bebe; font-family: Verdana;")
        self.institute_label.setFont(QFont("Verdana", 12, weight=QFont.Weight.DemiBold, italic=True))

        # New Class Button
        self.new_class_btn = QPushButton("New Class", self.central_widget)
        self.new_class_btn.setGeometry(521, 93, 89, 32)
        self.new_class_btn.setStyleSheet("background-color: #31cb1e; color: white; font-family: Verdana; font-size: 14px;")

        # Horizontal line
        self.line = QFrame(self.central_widget)
        self.line.setGeometry(22, 137, 588, 3)
        self.line.setStyleSheet("background-color: #1c1933;")

        # Create class blocks
        self.create_class_block(20, 168, "CLASS NAME", "Online")
        self.create_class_block(321, 168, "CLASS NAME", "Online")
        self.create_class_block(22, 255, "CLASS NAME", "Online")

    def create_class_block(self, x, y, class_name, status):
        # Background rectangle
        frame = QFrame(self.central_widget)
        frame.setGeometry(x, y, 287, 73)
        frame.setStyleSheet("background-color: #171529;")

        # Class image
        image = QLabel(frame)
        image.setGeometry(14, 8, 82, 57)
        image.setPixmap(QPixmap("template_image.png").scaled(82, 57, Qt.AspectRatioMode.KeepAspectRatio))
        image.setStyleSheet("background-color: transparent;")

        # Class name text
        name_label = QLabel(class_name, frame)
        name_label.setGeometry(100, 5, 171, 26)
        name_label.setStyleSheet("color: #ffffff; font-family: Verdana;")
        name_label.setFont(QFont("Verdana", 12, italic=True))

        # Status text
        status_label = QLabel(status, frame)
        status_label.setGeometry(221, 48, 58, 17)
        status_label.setStyleSheet("color: #ffffff;")
        status_label.setFont(QFont("Verdana", 12))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KamikochaanWindow()
    window.show()
    sys.exit(app.exec())