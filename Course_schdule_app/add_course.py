import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import os
from dotenv import load_dotenv
import mysql.connector as mysql
import add_session


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


class AddCourse(QWidget):

    def __init__(self):
        super(AddCourse, self).__init__()
        self.resize(700, 500)
        self.layouts()
        self.initUI()

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.label_layout = QVBoxLayout()
        self.course_layout = QFormLayout()
        self.course_layout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        self.main_layout.addLayout(self.label_layout, 10)
        self.main_layout.addLayout(self.course_layout, 90)
        self.setLayout(self.main_layout)

    def initUI(self):
        self.courses = QLabel("Add Course")
        self.courses.setStyleSheet("background:#414a4c;color:white")
        self.courses.setAlignment(Qt.AlignCenter)
        self.label_layout.addWidget(self.courses)

        course_name = QLabel("Course Name:")
        course_name_n = QLineEdit("course_name 1")
        description = QLabel("Description:")
        description_n = QLineEdit("Description 1")
        coach_name = QLabel("Coach Name:")
        coach_name_n = QLineEdit("Coach_Name1")

        btn_layout = QHBoxLayout()
        schedule_label = QLabel("Schedule")
        schedule_label.setStyleSheet("font:bold")
        btn_layout.addWidget(schedule_label)

        self.course_layout.addRow(course_name, course_name_n)
        self.course_layout.addRow(description, description_n)
        self.course_layout.addRow(coach_name, coach_name_n)
        self.course_layout.addRow(btn_layout)

        schedule_btn_layout = QHBoxLayout()
        schedule_btn = QPushButton("Add Schedule")
        schedule_btn.clicked.connect(self.onClickAddSchedule)
        schedule_btn_layout.addWidget(schedule_btn)
        self.course_layout.addRow(schedule_btn_layout)

        insidelayout = QHBoxLayout()
        add_btn_course = QPushButton("SAVE")
        # add_btn_course.clicked.connect(self.onClickSave)
        cancel_btn_session = QPushButton("CANCEL")
        cancel_btn_session.clicked.connect(self.onClickCancel)
        insidelayout.addWidget(add_btn_course)
        insidelayout.addWidget(cancel_btn_session)
        self.main_layout.addLayout(insidelayout)

        btn_layout.addStretch()
        schedule_btn_layout.addStretch()

    def onClickAddSchedule(self):
        self.obj=add_session.AddSessions()
        self.obj.show()
    
    def onClickCancel(self):
        self.hide()


def main():
    app = QApplication(sys.argv)
    ex = AddCourse()
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
