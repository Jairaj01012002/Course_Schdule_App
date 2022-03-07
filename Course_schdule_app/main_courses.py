import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import course_details
import add_course
import add_session


class MasterCourses(QWidget):

    def __init__(self):
        super(MasterCourses, self).__init__()
        self.layouts()
        self.initUI()

    def layouts(self):
        self.main_layout = QVBoxLayout()

        self.label_layout = QVBoxLayout()
        self.course_layout = QVBoxLayout()
        self.main_layout.addLayout(self.label_layout, 10)
        self.main_layout.addLayout(self.course_layout, 90)
        self.setLayout(self.main_layout)

    def initUI(self):
        self.courses = QLabel("All Courses")
        self.courses.setStyleSheet("background:#414a4c;color:white")
        self.courses.setAlignment(Qt.AlignCenter)
        self.label_layout.addWidget(self.courses)

        self.listWidget = QListWidget()
        add_btn_course = QPushButton("Add Course")
        add_btn_course.clicked.connect(self.onClickAddCourse)
        add_btn_session = QPushButton("Add Session")
        add_btn_session.clicked.connect(self.onClickAddSession)

        self.listWidget.addItem("Course 1")
        self.listWidget.addItem("Course 2")
        self.listWidget.addItem("Course 3")
        self.listWidget.itemDoubleClicked.connect(self.onClicked)
        self.course_layout.addWidget(self.listWidget)
        self.course_layout.addWidget(add_btn_course)
        self.course_layout.addWidget(add_btn_session)

    def onClicked(self, item):
        print(item.text())
        self.course_details = course_details.CourseDetails(item.text())
        delete_btn = self.course_details.add_btn_session
        delete_btn.clicked.connect(self.onClickDelete)
        self.course_details.show()
    
    def onClickDelete(self):
        self.course_details.hide()
        id = self.listWidget.currentRow()
        print(id)
        self.listWidget.takeItem(id)

    def onClickAddCourse(self):
        self.obj_course = add_course.AddCourse()
        self.obj_course.show()

    def onClickAddSession(self):
        self.obj_session = add_session.AddSessions()
        for_course = self.obj_session.course_layout

        combo_box=QComboBox()
        combo_box.addItems(["Course1", "Course2"])
        for_course.addRow(QLabel("For Course"), combo_box)
        self.obj_session.show()


def main():
    app = QApplication(sys.argv)
    ex = MasterCourses()
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
