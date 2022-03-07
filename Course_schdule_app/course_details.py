import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import os
from dotenv import load_dotenv
import mysql.connector as mysql
import session_details


load_dotenv()

try:
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd=os.getenv('password'),
        database="datacamp"
    )
    print("Connected to database...")
except Exception as e:
    print("Database not connected", e)
    sys.exit()

cursor = db.cursor()


class CourseDetails(QWidget):

    def __init__(self, course_name):
        super(CourseDetails, self).__init__()
        self.resize(700, 500)
        self.course_name = course_name
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
        self.courses = QLabel(self.course_name)
        self.courses.setStyleSheet("background:#414a4c;color:white")
        self.courses.setAlignment(Qt.AlignCenter)
        self.label_layout.addWidget(self.courses)

        course_name = QLabel("Course Name:")
        self.course_name_n = QLabel("course_name 1")
        description = QLabel("Description:")
        self.description_n = QLabel("Description 1")
        coach_name = QLabel("Coach Name:")
        self.coach_name_n = QLabel("Coach_Name1")

        btn_layout = QHBoxLayout()
        schedule_label = QLabel("Schedule")
        schedule_label.setStyleSheet("font:bold")
        btn_layout.addWidget(schedule_label)

        self.course_layout.addRow(course_name, self.course_name_n)
        self.course_layout.addRow(description, self.description_n)
        self.course_layout.addRow(coach_name, self.coach_name_n)
        # self.course_layout.addRow(inLayout)
        self.course_layout.addRow(btn_layout)

        schedule_list = []
        if not schedule_list:
            schedule_msg = QLabel("No Available Schedule")
            self.course_layout.addRow(schedule_msg)
        else:
            for schedule in schedule_list:
                schedule_btn = QPushButton(schedule)
                schedule_btn.clicked.connect(
                    lambda: self.onClickSessionDetails(schedule))
                self.course_layout.addRow(schedule_btn, QLabel("Date/Time"))

        insidelayout = QHBoxLayout()
        update_btn_course = QPushButton("UPDATE")
        update_btn_course.clicked.connect(self.onClickUpdate)

        self.add_btn_session = QPushButton("DELETE")
        insidelayout.addWidget(update_btn_course)
        insidelayout.addWidget(self.add_btn_session)
        self.main_layout.addLayout(insidelayout)

        btn_layout.addStretch()

    def onClickSessionDetails(self,schedule_name):
        print(f"{schedule_name}")
        self.obj = session_details.CourseDetails(schedule_name)
        self.obj.show()


    def onClickUpdate(self):
        print("Update")
        self.course_name_n = QLineEdit("course_name 1")
        self.description_n = QLineEdit("Description 1")
        self.coach_name_n = QLineEdit("Coach_Name1")


def main():
    app = QApplication(sys.argv)
    ex = CourseDetails("Course_Name_Details")
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
