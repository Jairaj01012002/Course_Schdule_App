import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import os
from dotenv import load_dotenv
import mysql.connector as mysql


load_dotenv()

try:
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd=os.getenv('password'),
        database="datacamp"
    )
    # print("Connected to database...")
except Exception as e:
    print("Database not connected", e)
    sys.exit()

cursor = db.cursor()


class AddSessions(QWidget):

    def __init__(self):
        super(AddSessions, self).__init__()
        self.resize(700, 500)
        self.layouts()
        self.initUI()

    def layouts(self):
        self.main_layout = QVBoxLayout()

        self.label_layout = QVBoxLayout()
        self.course_layout = QFormLayout()
        self.main_layout.addLayout(self.label_layout, 10)
        self.main_layout.addLayout(self.course_layout, 90)
        self.setLayout(self.main_layout)

    def initUI(self):
        self.courses = QLabel("Add Session")
        self.courses.setStyleSheet("background:#414a4c;color:white")
        self.courses.setAlignment(Qt.AlignCenter)
        self.label_layout.addWidget(self.courses)

        title = QLabel("Title:")
        title_n = QLineEdit("Title1")
        description = QLabel("Description:")
        description_n = QLineEdit("Description1")
        link = QLabel("Link:")
        link_n = QLineEdit("Link1")

        start = QLabel("Start: ")
        start_time = QLabel("Date/Time")
        start_time = QCalendarWidget()
        start_time.setGridVisible(True)
        # start_time.setMinimumDate(QDate(currentDate, currentMonth-1, 1))
        start_time.clicked.connect(self.printStartTime)

        end = QLabel("End: ")
        end_time = QLabel("Date/Time")
        end_time = QCalendarWidget()
        end_time.setGridVisible(True)
        end_time.clicked.connect(self.printEndTime)

        self.course_layout.addRow(title, title_n)
        self.course_layout.addRow(description, description_n)
        self.course_layout.addRow(link, link_n)
        self.course_layout.addRow(start, start_time)
        self.course_layout.addRow(end, end_time)

        add_btn_course = QPushButton("ADD")
        add_btn_session = QPushButton("CANCEL")
        insidelayout = QHBoxLayout()
        insidelayout.addWidget(add_btn_course)
        insidelayout.addWidget(add_btn_session)
        self.main_layout.addLayout(insidelayout)

    def printStartTime(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))

    def printEndTime(self,qDate):
        print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))


def main():
    app = QApplication(sys.argv)
    ex = AddSessions()
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
