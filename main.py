# This programme is created to serve TIU IRSA's Trivia Night and is open source

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from time import sleep


#  Open the edit box for the themes
class ThemeBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 380)
        self.setWindowTitle('Theme Change')
        self.themebox_gui()

    def themebox_gui(self):
        self.theme_1 = QtWidgets.QLabel(self)
        self.theme_1.setGeometry(10, 40, 70, 25)
        self.theme_1.setText('Theme 1:')
        self.theme_1.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_2 = QtWidgets.QLabel(self)
        self.theme_2.setGeometry(10, 90, 70, 25)
        self.theme_2.setText('Theme 2:')
        self.theme_2.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_3 = QtWidgets.QLabel(self)
        self.theme_3.setGeometry(10, 140, 70, 25)
        self.theme_3.setText('Theme 3:')
        self.theme_3.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_4 = QtWidgets.QLabel(self)
        self.theme_4.setGeometry(10, 190, 70, 25)
        self.theme_4.setText('Theme 4:')
        self.theme_4.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_5 = QtWidgets.QLabel(self)
        self.theme_5.setGeometry(10, 240, 70, 25)
        self.theme_5.setText('Theme 5:')
        self.theme_5.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_name_1 = QtWidgets.QTextEdit(self)
        self.theme_name_1.setGeometry(90, 30, 300, 40)
        self.theme_name_1.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_name_2 = QtWidgets.QTextEdit(self)
        self.theme_name_2.setGeometry(90, 80, 300, 40)
        self.theme_name_2.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_name_3 = QtWidgets.QTextEdit(self)
        self.theme_name_3.setGeometry(90, 130, 300, 40)
        self.theme_name_3.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_name_4 = QtWidgets.QTextEdit(self)
        self.theme_name_4.setGeometry(90, 180, 300, 40)
        self.theme_name_4.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.theme_name_5 = QtWidgets.QTextEdit(self)
        self.theme_name_5.setGeometry(90, 230, 300, 40)
        self.theme_name_5.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.save_option = QtWidgets.QPushButton(self)
        self.save_option.setGeometry(50, 310, 100, 30)
        self.save_option.setText('Save')
        self.save_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.cancel_option = QtWidgets.QPushButton(self)
        self.cancel_option.setGeometry(250, 310, 100, 30)
        self.cancel_option.setText('Cancel')
        self.cancel_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #  Actions when buttons are pressed:
        self.cancel_option.clicked.connect(lambda: self.close())

    #  Functions for the buttons
    def get_theme_1(self):
        self.new_theme_1 = self.theme_name_1.toPlainText()
        return self.new_theme_1

    def get_theme_2(self):
        self.new_theme_2 = self.theme_name_2.toPlainText()
        return self.new_theme_2

    def get_theme_3(self):
        self.new_theme_3 = self.theme_name_3.toPlainText()
        return self.new_theme_3

    def get_theme_4(self):
        self.new_theme_4 = self.theme_name_4.toPlainText()
        return self.new_theme_4

    def get_theme_5(self):
        self.new_theme_5 = self.theme_name_5.toPlainText()
        return self.new_theme_5


#  Open the edit box to edit the answers and questions and write to txt file
class EditBox(QtWidgets.QWidget):
    def __init__(self, position):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle('Edit Question & Answer')
        self.position = position
        self.edit_box_gui(self.position)

    def edit_box_gui(self, position):
        self.new_question = QtWidgets.QLabel(self)
        self.new_question.setGeometry(295, 50, 110, 25)
        self.new_question.setText('New Question')
        self.new_question.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.new_answer = QtWidgets.QLabel(self)
        self.new_answer.setGeometry(300, 190, 100, 20)
        self.new_answer.setText('New Answer')
        self.new_answer.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.question_box = QtWidgets.QTextEdit(self)
        self.question_box.setGeometry(50, 80, 600, 80)
        self.question_box.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.answer_box = QtWidgets.QTextEdit(self)
        self.answer_box.setGeometry(50, 220, 600, 80)
        self.answer_box.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.save_option = QtWidgets.QPushButton(self)
        self.save_option.setGeometry(125, 330, 100, 30)
        self.save_option.setText('Save')
        self.save_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.cancel_option = QtWidgets.QPushButton(self)
        self.cancel_option.setGeometry(450, 330, 100, 30)
        self.cancel_option.setText('Cancel')
        self.cancel_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #  Actions when buttons are pressed:
        self.save_option.clicked.connect(lambda: self.save_operation(position))
        self.cancel_option.clicked.connect(lambda: self.close())

    #  Fuctions for the Edit box:
    def save_operation(self, position):
        self.question_text = self.question_box.toPlainText()
        self.answer_text = self.answer_box.toPlainText()
        with open('questions.txt', 'r+') as f_question:
            data = f_question.readlines()
            data[position] = self.question_text
            f_question.seek(0, 0)
            f_question.writelines(data)
        with open('answers.txt', 'r+') as f_answer:
            data2 = f_answer.readlines()
            data2[position] = self.answer_text
            f_answer.seek(0, 0)
            f_answer.writelines(data2)
        self.close()


class NameChangeDialogue(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('Team Name Change')
        self.name_change_dialogue_gui()

    def name_change_dialogue_gui(self):
        self.new_name = QtWidgets.QLabel(self)
        self.new_name.setGeometry(160, 40, 82, 30)
        self.new_name.setText('New Name')
        self.new_name.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.name_change_box = QtWidgets.QTextEdit(self)
        self.name_change_box.setGeometry(90, 100, 220, 90)
        self.name_change_box.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.save_option = QtWidgets.QPushButton(self)
        self.save_option.setGeometry(50, 230, 100, 30)
        self.save_option.setText('Save')
        self.save_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.cancel_option = QtWidgets.QPushButton(self)
        self.cancel_option.setGeometry(250, 230, 100, 30)
        self.cancel_option.setText('Cancel')
        self.cancel_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #  Actions when buttons are pressed:
        self.save_option.clicked.connect(self.get_new_name)
        self.cancel_option.clicked.connect(lambda: self.close())

    #  Actions for the name change dialogue box:
    def get_new_name(self):
        self.new_name_change = self.name_change_box.toPlainText()
        self.close()

    def pass_new_name(self):
        return self.new_name_change


class Count_Down(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(str)

    def counter(self, time):
        while time >= 0:
            minute, second = divmod(time, 60)
            QtWidgets.qApp.processEvents()
            sleep(1)
            time -= 1
            self.progress.emit('{:02d}:{:02d}'.format(minute, second))
        self.finished.emit()


class Timer_Box(QtWidgets.QWidget):
    def __init__(self, minute, second):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('Timer')
        self.time = minute * 60 + second
        self.timer_gui()
        self.longtask()

    def timer_gui(self):
        self.clock = QtWidgets.QLabel(self)
        self.clock.setGeometry(130, 110, 140, 60)
        self.clock.setFont(QtGui.QFont('Baskerville Old Face', 36))

        self.close_window = QtWidgets.QPushButton(self)
        self.close_window.setGeometry(155, 210, 90, 30)
        self.close_window.setText('Close')

        self.close_window.clicked.connect(self.close_function)

    def longtask(self):
        self.thread = QtCore.QThread()
        self.worker = Count_Down()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(lambda: self.worker.counter(self.time))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_clock)
        self.worker.finished.connect(lambda: self.close())
        self.thread.start()

    def update_clock(self, time):
        self.clock.setText(time)

    def close_function(self):
        self.close()


class Q_and_A_Box(QtWidgets.QWidget):
    def __init__(self, position):
        super().__init__()
        self.resize(1920, 1040)
        self.setWindowTitle('Question and Answer')
        self.setStyleSheet("background-color: rgb(20, 129, 119);")
        self.position, self.question_text, self.answer_text = position, str(), str()
        self.get_data()
        self.qagui()

    def get_data(self):
        with open('questions.txt', 'r') as f_question:
            data_question = f_question.readlines()
            if data_question[self.position] == '\n':
                self.question_text = "There isn't anything here! This is a placeholder text"
            else:
                self.question_text = data_question[self.position]
        with open('answers.txt', 'r') as f_answer:
            data_answer = f_answer.readlines()
            if data_answer[self.position] == '\n':
                self.answer_text = "There isn't anything here! This is a placeholder text"
            else:
                self.answer_text = data_answer[self.position]

    def qagui(self):
        self.gobackbutton = QtWidgets.QPushButton(self)
        self.gobackbutton.setGeometry(60, 60, 90, 30)
        self.gobackbutton.setText('Go Back')
        self.gobackbutton.setStyleSheet('color: rgb(255, 255, 255);')
        self.gobackbutton.setFont(QtGui.QFont('Baskerville Old Face', 11))

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(0, 540, 1920, 16)
        self.line.setStyleSheet('color: rgb(129, 20, 30)')
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 140, 1220, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.question_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font1 = QtGui.QFont()
        font1.setFamily(u"Baskerville Old Face")
        font1.setPointSize(28)
        self.question_label.setFont(font1)
        self.question_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setText(self.question_text)
        self.question_label.setWordWrap(True)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(350, 600, 1220, 200))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.answer_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.answer_label.setFont(font1)
        self.answer_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setText(self.answer_text)
        self.answer_label.setWordWrap(True)
        self.answer_label.hide()

        self.timer = QtWidgets.QTimeEdit(self)
        self.timer.setGeometry(900, 350, 120, 40)
        self.timer.setFont(QtGui.QFont('Baskerville Old Face', 18))
        self.timer.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.timer.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 1, 0)))
        self.timer.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timer.setDisplayFormat('mm:ss')

        self.timer_start = QtWidgets.QPushButton(self)
        self.timer_start.setGeometry(835, 450, 95, 30)
        self.timer_start.setFont(QtGui.QFont('Baskerville Old Face', 11))
        self.timer_start.setStyleSheet('background-color: rgb(230, 230, 230)')
        self.timer_start.setText('Start Timer')

        self.show_answer = QtWidgets.QPushButton(self)
        self.show_answer.setGeometry(990, 450, 105, 30)
        self.show_answer.setFont(QtGui.QFont('Baskerville Old Face', 11))
        self.show_answer.setStyleSheet('background-color: rgb(230, 230, 230)')
        self.show_answer.setText('Show Answer')

        self.give_point_button = QtWidgets.QPushButton(self)
        self.give_point_button.setGeometry(430, 870, 130, 40)
        self.give_point_button.setFont(QtGui.QFont('Baskerville Old Face', 14))
        self.give_point_button.setStyleSheet('color: rgb(255, 255, 255);\n'
                                             'background-color: rgb(129, 20, 30);')
        self.give_point_button.setText('Give Points')
        self.give_point_button.hide()

        self.no_point_button = QtWidgets.QPushButton(self)
        self.no_point_button.setGeometry(1360, 870, 130, 40)
        self.no_point_button.setFont(QtGui.QFont('Baskerville Old Face', 14))
        self.no_point_button.setStyleSheet('color: rgb(255, 255, 255);\n'
                                           'background-color: rgb(129, 20, 30);')
        self.no_point_button.setText('No Points')
        self.no_point_button.hide()

        self.score = 0

        self.horizontalLayout.addWidget(self.question_label)
        self.horizontalLayout_2.addWidget(self.answer_label)

        #  Actions when buttons are pressed:
        self.gobackbutton.clicked.connect(lambda: self.close())

        self.timer_start.clicked.connect(self.get_current_time)

        self.show_answer.clicked.connect(self.open_answer_box)

        self.give_point_button.clicked.connect(self.scored)
        self.no_point_button.clicked.connect(self.no_scored)

    #  Usuable functions for button pressed:
    def get_current_time(self):
        minute = self.timer.time().minute()
        second = self.timer.time().second()
        self.open_timer(minute, second)

    def open_answer_box(self):
        self.answer_label.show()
        self.give_point_button.show()
        self.no_point_button.show()

    def open_timer(self, minute, second):
        self.timer_box = Timer_Box(minute, second)
        self.timer_box.show()

    def scored(self):
        self.score = ((self.position % 5) + 1) * 100
        self.close()

    def no_scored(self):
        self.score = 0
        self.close()

    def get_scored(self):
        return self.score


class End_Game(QtWidgets.QWidget):
    def __init__(self, team, score):
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Winner")
        self.setStyleSheet('background-color: rgb(20, 129, 119)')
        self.team, self.score = team, score
        self.end_game_gui()

    def end_game_gui(self):
        self.winner_label = QtWidgets.QLabel(self)
        self.winner_label.setGeometry(QtCore.QRect(245, 70, 110, 60))
        self.winner_label.setFont(QtGui.QFont('Baskerville Old Face', 20))
        self.winner_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.winner_label.setText('Winner!')

        self.horizontallayouwidget = QtWidgets.QWidget(self)
        self.horizontallayouwidget.setGeometry(QtCore.QRect(0, 130, 600, 80))
        self.horizontallayour = QtWidgets.QHBoxLayout(self.horizontallayouwidget)
        self.horizontallayour.setContentsMargins(0, 0, 0, 0)

        self.name_label = QtWidgets.QLabel(self.horizontallayouwidget)
        self.name_label.setFont(QtGui.QFont('Baskerville Old Face', 28))
        self.name_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setText(self.team)

        self.with_label = QtWidgets.QLabel(self)
        self.with_label.setGeometry(QtCore.QRect(275, 220, 50, 45))
        self.with_label.setFont(QtGui.QFont('Baskerville Old Face', 14))
        self.with_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.with_label.setText('With')

        self.horizontallayouwidget2 = QtWidgets.QWidget(self)
        self.horizontallayouwidget2.setGeometry(QtCore.QRect(0, 270, 600, 80))
        self.horizontallayour2 = QtWidgets.QHBoxLayout(self.horizontallayouwidget2)
        self.horizontallayour2.setContentsMargins(0, 0, 0, 0)

        self.score_label = QtWidgets.QLabel(self.horizontallayouwidget2)
        self.score_label.setFont(QtGui.QFont('Baskerville Old Face', 28))
        self.score_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.score_label.setText(str(self.score) + ' Points')

        self.horizontallayour.addWidget(self.name_label)
        self.horizontallayour2.addWidget(self.score_label)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        current_path = os.getcwd()
        os.chdir(current_path)
        self.editmode_state = False
        self.score1_num, self.score2_num, self.team_in_turn = 0, 0, 0
        self.check_questions_txt()
        self.check_answers_txt()
        self.setupUi()

    def check_questions_txt(self):
        with open('questions.txt', 'w+') as f:
            data = f.readlines()
            for i in range(25):
                try:
                    if data[i] != "":
                        pass
                except IndexError:
                    data += ['\n']
            f.seek(0, 0)
            f.writelines(data)

    def check_answers_txt(self):
        with open('answers.txt', 'w+') as f:
            data = f.readlines()
            for i in range(25):
                try:
                    if data[i] != "":
                        pass
                except IndexError:
                    data += ['\n']
            f.seek(0, 0)
            f.writelines(data)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: rgb(20, 129, 119);")

        self.centralwidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1921, 931))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(15, 0, 15, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.theme_button = QtWidgets.QPushButton(self)
        self.theme_button.setGeometry(15, 114, 150, 30)
        self.theme_button.setText('Change Themes')
        self.theme_button.setFont(QtGui.QFont('Baskerville Old Face', 11))
        self.theme_button.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(202, 202, 202);")
        self.theme_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.theme_button.setStatusTip('Press to change the themes')
        self.theme_button.hide()

        self.introduction = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.introduction.sizePolicy().hasHeightForWidth())
        self.introduction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.introduction.setFont(font)
        self.introduction.setStyleSheet("color: rgb(255, 255, 255);")
        self.introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.introduction.setObjectName("introduction")
        self.gridLayout.addWidget(self.introduction, 0, 0, 1, 5)

        self.theme1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme1.sizePolicy().hasHeightForWidth())
        self.theme1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.theme1.setFont(font)
        self.theme1.setStyleSheet("color: rgb(255, 255, 255);")
        self.theme1.setAlignment(QtCore.Qt.AlignCenter)
        self.theme1.setObjectName("theme1")
        self.gridLayout.addWidget(self.theme1, 1, 0, 1, 1)

        self.theme2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme2.sizePolicy().hasHeightForWidth())
        self.theme2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.theme2.setFont(font)
        self.theme2.setStyleSheet("color: rgb(255, 255, 255);")
        self.theme2.setAlignment(QtCore.Qt.AlignCenter)
        self.theme2.setObjectName("theme2")
        self.gridLayout.addWidget(self.theme2, 1, 1, 1, 1)

        self.theme3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme3.sizePolicy().hasHeightForWidth())
        self.theme3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.theme3.setFont(font)
        self.theme3.setStyleSheet("color: rgb(255, 255, 255);")
        self.theme3.setAlignment(QtCore.Qt.AlignCenter)
        self.theme3.setObjectName("theme3")
        self.gridLayout.addWidget(self.theme3, 1, 2, 1, 1)

        self.theme4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme4.sizePolicy().hasHeightForWidth())
        self.theme4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.theme4.setFont(font)
        self.theme4.setStyleSheet("color: rgb(255, 255, 255);")
        self.theme4.setAlignment(QtCore.Qt.AlignCenter)
        self.theme4.setObjectName("theme4")
        self.gridLayout.addWidget(self.theme4, 1, 3, 1, 1)

        self.theme5 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme5.sizePolicy().hasHeightForWidth())
        self.theme5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.theme5.setFont(font)
        self.theme5.setStyleSheet("color: rgb(255, 255, 255);")
        self.theme5.setAlignment(QtCore.Qt.AlignCenter)
        self.theme5.setObjectName("theme5")
        self.gridLayout.addWidget(self.theme5, 1, 4, 1, 1)

        self.button_1_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1_1.sizePolicy().hasHeightForWidth())
        self.button_1_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_1_1.setFont(font)
        self.button_1_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_1_1.setObjectName("button_1_1")
        self.button_1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_1_1, 2, 0, 1, 1)

        self.button_1_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1_2.sizePolicy().hasHeightForWidth())
        self.button_1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_1_2.setFont(font)
        self.button_1_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_1_2.setObjectName("button_1_2")
        self.button_1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_1_2, 3, 0, 1, 1)

        self.button_1_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1_3.sizePolicy().hasHeightForWidth())
        self.button_1_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_1_3.setFont(font)
        self.button_1_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_1_3.setObjectName("button_1_3")
        self.button_1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_1_3, 4, 0, 1, 1)

        self.button_1_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1_4.sizePolicy().hasHeightForWidth())
        self.button_1_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_1_4.setFont(font)
        self.button_1_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_1_4.setObjectName("button_1_4")
        self.button_1_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_1_4, 5, 0, 1, 1)

        self.button_1_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1_5.sizePolicy().hasHeightForWidth())
        self.button_1_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_1_5.setFont(font)
        self.button_1_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_1_5.setObjectName("button_1_5")
        self.button_1_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_1_5, 6, 0, 1, 1)

        self.button_2_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2_1.sizePolicy().hasHeightForWidth())
        self.button_2_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_2_1.setFont(font)
        self.button_2_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_2_1.setObjectName("button_2_1")
        self.button_2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_2_1, 2, 1, 1, 1)

        self.button_2_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2_2.sizePolicy().hasHeightForWidth())
        self.button_2_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_2_2.setFont(font)
        self.button_2_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_2_2.setObjectName("button_2_2")
        self.button_2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_2_2, 3, 1, 1, 1)

        self.button_2_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2_3.sizePolicy().hasHeightForWidth())
        self.button_2_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_2_3.setFont(font)
        self.button_2_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_2_3.setObjectName("button_2_3")
        self.button_2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_2_3, 4, 1, 1, 1)

        self.button_2_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2_4.sizePolicy().hasHeightForWidth())
        self.button_2_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_2_4.setFont(font)
        self.button_2_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_2_4.setObjectName("button_2_4")
        self.button_2_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_2_4, 5, 1, 1, 1)

        self.button_2_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2_5.sizePolicy().hasHeightForWidth())
        self.button_2_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_2_5.setFont(font)
        self.button_2_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_2_5.setObjectName("button_2_5")
        self.button_2_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_2_5, 6, 1, 1, 1)

        self.button_3_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3_1.sizePolicy().hasHeightForWidth())
        self.button_3_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_3_1.setFont(font)
        self.button_3_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_3_1.setObjectName("button_3_1")
        self.button_3_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_3_1, 2, 2, 1, 1)

        self.button_3_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3_2.sizePolicy().hasHeightForWidth())
        self.button_3_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_3_2.setFont(font)
        self.button_3_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_3_2.setObjectName("button_3_2")
        self.button_3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_3_2, 3, 2, 1, 1)

        self.button_3_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3_3.sizePolicy().hasHeightForWidth())
        self.button_3_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_3_3.setFont(font)
        self.button_3_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_3_3.setObjectName("button_3_3")
        self.button_3_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_3_3, 4, 2, 1, 1)

        self.button_3_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3_4.sizePolicy().hasHeightForWidth())
        self.button_3_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_3_4.setFont(font)
        self.button_3_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_3_4.setObjectName("button_3_4")
        self.button_3_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_3_4, 5, 2, 1, 1)

        self.button_3_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3_5.sizePolicy().hasHeightForWidth())
        self.button_3_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_3_5.setFont(font)
        self.button_3_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_3_5.setObjectName("button_3_5")
        self.button_3_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_3_5, 6, 2, 1, 1)

        self.button_4_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4_1.sizePolicy().hasHeightForWidth())
        self.button_4_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_4_1.setFont(font)
        self.button_4_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_4_1.setObjectName("button_4_1")
        self.button_4_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_4_1, 2, 3, 1, 1)

        self.button_4_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4_2.sizePolicy().hasHeightForWidth())
        self.button_4_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_4_2.setFont(font)
        self.button_4_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_4_2.setObjectName("button_4_2")
        self.button_4_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_4_2, 3, 3, 1, 1)

        self.button_4_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4_3.sizePolicy().hasHeightForWidth())
        self.button_4_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_4_3.setFont(font)
        self.button_4_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_4_3.setObjectName("button_4_3")
        self.button_4_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_4_3, 4, 3, 1, 1)

        self.button_4_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4_4.sizePolicy().hasHeightForWidth())
        self.button_4_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_4_4.setFont(font)
        self.button_4_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_4_4.setObjectName("button_4_4")
        self.button_4_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_4_4, 5, 3, 1, 1)

        self.button_4_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4_5.sizePolicy().hasHeightForWidth())
        self.button_4_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_4_5.setFont(font)
        self.button_4_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_4_5.setObjectName("button_4_5")
        self.button_4_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_4_5, 6, 3, 1, 1)

        self.button_5_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5_1.sizePolicy().hasHeightForWidth())
        self.button_5_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_5_1.setFont(font)
        self.button_5_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_5_1.setObjectName("button_5_1")
        self.button_5_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_5_1, 2, 4, 1, 1)

        self.button_5_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5_2.sizePolicy().hasHeightForWidth())
        self.button_5_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_5_2.setFont(font)
        self.button_5_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_5_2.setObjectName("button_5_2")
        self.button_5_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_5_2, 3, 4, 1, 1)

        self.button_5_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5_3.sizePolicy().hasHeightForWidth())
        self.button_5_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_5_3.setFont(font)
        self.button_5_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_5_3.setObjectName("button_5_3")
        self.button_5_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_5_3, 4, 4, 1, 1)

        self.button_5_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5_4.sizePolicy().hasHeightForWidth())
        self.button_5_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_5_4.setFont(font)
        self.button_5_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_5_4.setObjectName("button_5_4")
        self.button_5_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_5_4, 5, 4, 1, 1)

        self.button_5_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5_5.sizePolicy().hasHeightForWidth())
        self.button_5_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.button_5_5.setFont(font)
        self.button_5_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(129, 20, 30);")
        self.button_5_5.setObjectName("button_5_5")
        self.button_5_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.button_5_5, 6, 4, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.team2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team2.sizePolicy().hasHeightForWidth())
        self.team2.setSizePolicy(sizePolicy)
        self.team2.setMaximumSize(QtCore.QSize(250, 52))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(11)
        self.team2.setFont(font)
        self.team2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(129, 20, 30);")
        self.team2.setObjectName("team2")
        self.team2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_2.addWidget(self.team2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.score2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score2.sizePolicy().hasHeightForWidth())
        self.score2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.score2.setFont(font)
        self.score2.setStyleSheet("color: rgb(255, 255, 255);")
        self.score2.setAlignment(QtCore.Qt.AlignCenter)
        self.score2.setObjectName("score2")
        self.verticalLayout_2.addWidget(self.score2)
        self.gridLayout.addLayout(self.verticalLayout_2, 7, 3, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.team1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team1.sizePolicy().hasHeightForWidth())
        self.team1.setSizePolicy(sizePolicy)
        self.team1.setMaximumSize(QtCore.QSize(250, 52))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(11)
        self.team1.setFont(font)
        self.team1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(129, 20, 30);")
        self.team1.setObjectName("team1")
        self.team1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.team1)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.score1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score1.sizePolicy().hasHeightForWidth())
        self.score1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.score1.setFont(font)
        self.score1.setStyleSheet("color: rgb(255, 255, 255);")
        self.score1.setAlignment(QtCore.Qt.AlignCenter)
        self.score1.setObjectName("score1")
        self.verticalLayout.addWidget(self.score1)
        self.gridLayout.addLayout(self.verticalLayout, 7, 1, 1, 1)

        self.endgame = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endgame.sizePolicy().hasHeightForWidth())
        self.endgame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        self.endgame.setFont(font)
        self.endgame.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(129, 20, 30);")
        self.endgame.setObjectName("endgame")
        self.endgame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.endgame, 7, 2, 1, 1)
        self.endgame.hide()

        self.editmode_indicator = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(11)
        self.editmode_indicator.setFont(font)
        self.editmode_indicator.setStyleSheet("color: rgb(255, 231, 90);")
        self.editmode_indicator.setAlignment(QtCore.Qt.AlignCenter)
        self.editmode_indicator.setObjectName("editmode_indicator")
        self.gridLayout.addWidget(self.editmode_indicator, 7, 0, 1, 1)
        self.editmode_indicator.hide()

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuSomething = QtWidgets.QMenu(self.menubar)
        self.menuSomething.setObjectName("menuSomething")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(self)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave_staet = QtWidgets.QAction(self)
        self.actionSave_staet.setObjectName("actionSave_staet")

        self.actionClose_window = QtWidgets.QAction(self)
        self.actionClose_window.setObjectName("actionClose_window")
        self.actionClose_window.setStatusTip('Press the close the programme')
        self.actionClose_window.setShortcut(QtGui.QKeySequence("Esc"))

        self.actionToggle_edit_mode_on = QtWidgets.QAction(self)
        self.actionToggle_edit_mode_on.setObjectName("actionToggle_edit_mode_on")
        self.actionToggle_edit_mode_on.setStatusTip('Press to toggle edit mode on/off')
        self.actionToggle_edit_mode_on.setShortcut(QtGui.QKeySequence("Ctrl+E"))

        self.menuSomething.addAction(self.actionOpen_file)
        self.menuSomething.addAction(self.actionSave_staet)
        self.menuSomething.addAction(self.actionClose_window)
        self.menuEdit.addAction(self.actionToggle_edit_mode_on)
        self.menubar.addAction(self.menuSomething.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        #  Actions when the actions in the menubar "File" is pressed:
        self.actionClose_window.triggered.connect(self.close_window)

        #  Actions when the action in the menubar "Edit is pressed:
        self.actionToggle_edit_mode_on.triggered.connect(self.editmode_toggle)
        self.theme_button.clicked.connect(self.when_theme_clicked)

        #  Action when the game buttons are pressed:
        self.button_1_1.clicked.connect(lambda: self.when_clicked(0))
        self.button_1_2.clicked.connect(lambda: self.when_clicked(1))
        self.button_1_3.clicked.connect(lambda: self.when_clicked(2))
        self.button_1_4.clicked.connect(lambda: self.when_clicked(3))
        self.button_1_5.clicked.connect(lambda: self.when_clicked(4))
        self.button_2_1.clicked.connect(lambda: self.when_clicked(5))
        self.button_2_2.clicked.connect(lambda: self.when_clicked(6))
        self.button_2_3.clicked.connect(lambda: self.when_clicked(7))
        self.button_2_4.clicked.connect(lambda: self.when_clicked(8))
        self.button_2_5.clicked.connect(lambda: self.when_clicked(9))
        self.button_3_1.clicked.connect(lambda: self.when_clicked(10))
        self.button_3_2.clicked.connect(lambda: self.when_clicked(11))
        self.button_3_3.clicked.connect(lambda: self.when_clicked(12))
        self.button_3_4.clicked.connect(lambda: self.when_clicked(13))
        self.button_3_5.clicked.connect(lambda: self.when_clicked(14))
        self.button_4_1.clicked.connect(lambda: self.when_clicked(15))
        self.button_4_2.clicked.connect(lambda: self.when_clicked(16))
        self.button_4_3.clicked.connect(lambda: self.when_clicked(17))
        self.button_4_4.clicked.connect(lambda: self.when_clicked(18))
        self.button_4_5.clicked.connect(lambda: self.when_clicked(19))
        self.button_5_1.clicked.connect(lambda: self.when_clicked(20))
        self.button_5_2.clicked.connect(lambda: self.when_clicked(21))
        self.button_5_3.clicked.connect(lambda: self.when_clicked(22))
        self.button_5_4.clicked.connect(lambda: self.when_clicked(23))
        self.button_5_5.clicked.connect(lambda: self.when_clicked(24))

        #  Actions when the team name buttons are pressed:
        self.team1.clicked.connect(lambda: self.when_name_clicked(1))
        self.team2.clicked.connect(lambda: self.when_name_clicked(2))

        #  Action when end game button is clicked:
        self.endgame.clicked.connect(self.end_clicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "TIU IRSA Trivia Night  v.1.0"))
        self.button_5_4.setText(_translate("MainWindow", "400"))
        self.theme5.setText(_translate("MainWindow", "Theme 5"))
        self.button_4_2.setText(_translate("MainWindow", "200"))
        self.button_4_5.setText(_translate("MainWindow", "500"))
        self.theme4.setText(_translate("MainWindow", "Theme 4"))
        self.button_4_3.setText(_translate("MainWindow", "300"))
        self.button_3_5.setText(_translate("MainWindow", "500"))
        self.button_3_2.setText(_translate("MainWindow", "200"))
        self.button_1_4.setText(_translate("MainWindow", "400"))
        self.button_4_4.setText(_translate("MainWindow", "400"))
        self.button_5_3.setText(_translate("MainWindow", "300"))
        self.button_3_4.setText(_translate("MainWindow", "400"))
        self.button_2_4.setText(_translate("MainWindow", "400"))
        self.button_1_5.setText(_translate("MainWindow", "500"))
        self.button_2_5.setText(_translate("MainWindow", "500"))
        self.theme3.setText(_translate("MainWindow", "Theme 3"))
        self.button_5_5.setText(_translate("MainWindow", "500"))
        self.team2.setText(_translate("MainWindow", "Team 2"))
        self.score2.setText(_translate("MainWindow", str(self.score2_num)))
        self.theme2.setText(_translate("MainWindow", "Theme 2"))
        self.button_2_2.setText(_translate("MainWindow", "200"))
        self.button_3_1.setText(_translate("MainWindow", "100"))
        self.team1.setText(_translate("MainWindow", "Team 1"))
        self.score1.setText(_translate("MainWindow", str(self.score1_num)))
        self.button_2_3.setText(_translate("MainWindow", "300"))
        self.button_2_1.setText(_translate("MainWindow", "100"))
        self.theme1.setText(_translate("MainWindow", "Theme 1"))
        self.button_1_2.setText(_translate("MainWindow", "200"))
        self.button_1_1.setText(_translate("MainWindow", "100"))
        self.button_1_3.setText(_translate("MainWindow", "300"))
        self.button_5_2.setText(_translate("MainWindow", "200"))
        self.button_5_1.setText(_translate("MainWindow", "100"))
        self.introduction.setText(_translate("MainWindow", "TIU IRSA TRIVIA NIGHT"))
        self.button_3_3.setText(_translate("MainWindow", "300"))
        self.button_4_1.setText(_translate("MainWindow", "100"))
        self.endgame.setText(_translate("MainWindow", "End the Game"))
        self.editmode_indicator.setText(_translate("MainWindow", "Edit Mode On"))
        self.menuSomething.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionSave_staet.setText(_translate("MainWindow", "Save state"))
        self.actionClose_window.setText(_translate("MainWindow", "Close window"))
        self.actionToggle_edit_mode_on.setText(_translate("MainWindow", "Toggle edit mode"))

    #  Usuable functions for the menu bar "File"
    def close_window(self):
        self.close()

    #  Usuable functions for the menu bar "Edit"
    def editmode_toggle(self):
        if self.editmode_state == False:
            self.editmode_indicator.show()
            self.theme_button.show()
        else:
            self.editmode_indicator.hide()
            self.theme_button.hide()
        self.editmode_state = not self.editmode_state

    #  Usuable functions for the theme editor:
    def when_theme_clicked(self):
        self.themebox = ThemeBox()
        self.themebox.show()
        self.themebox.save_option.clicked.connect(self.theme_change)

    def theme_change(self):
        self.theme1.setText(self.themebox.get_theme_1())
        self.theme2.setText(self.themebox.get_theme_2())
        self.theme3.setText(self.themebox.get_theme_3())
        self.theme4.setText(self.themebox.get_theme_4())
        self.theme5.setText(self.themebox.get_theme_5())
        self.themebox.close()

    #  Usuable functions for the game buttons:
    def when_clicked(self, position):
        if self.editmode_state == True:
            self.game_edit(position)
        else:
            self.gameplay(position)

    def game_edit(self, position):
        self.edit_box = EditBox(position)
        self.edit_box.show()

    def gameplay(self, position):
        self.game_box = Q_and_A_Box(position)
        self.game_box.show()
        self.game_box.give_point_button.clicked.connect(self.getpoint)
        self.game_box.no_point_button.clicked.connect(lambda: self.game_box.close())

    def getpoint(self):
        if self.team_in_turn == 1:
            self.score1_num += self.game_box.get_scored()
            self.score1.setText(str(self.score1_num))
            self.set_team_state(2)
        else:
            self.score2_num += self.game_box.get_scored()
            self.score2.setText(str(self.score2_num))
            self.set_team_state(1)

    #  Usuable functions for team names:
    def when_name_clicked(self, team):
        if self.editmode_state == True:
            self.name_change(team)
        else:
            self.set_team_state(team)
            self.endgame.show()

    def name_change(self, team):
        self.name_change_dialogue_box = NameChangeDialogue()
        self.name_change_dialogue_box.show()
        if team == 1:
            self.name_change_dialogue_box.save_option.clicked.connect(lambda:
                                                                      self.team1.setText(
                                                                          self.name_change_dialogue_box.
                                                                              pass_new_name()
                                                                      ))
        else:
            self.name_change_dialogue_box.save_option.clicked.connect(lambda:
                                                                      self.team2.setText(
                                                                          self.name_change_dialogue_box.
                                                                              pass_new_name()
                                                                      ))

    def set_team_state(self, team):
        if team == 1:
            self.team1.setStyleSheet('background-color: rgb(255, 218, 83);\n'
                                     'color: rgb(0, 0, 0);')
            self.team2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(129, 20, 30);")
        else:
            self.team2.setStyleSheet('background-color: rgb(255, 218, 83);\n'
                                     'color: rgb(0, 0, 0);')
            self.team1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(129, 20, 30);")
        self.team_in_turn = team

    #  Usuable function for the end game button:
    def end_clicked(self):
        self.team1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(129, 20, 30);")
        self.team2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(129, 20, 30);")
        if self.score1_num > self.score2_num:
            self.end_game_screen = End_Game(self.team1.text(), self.score1_num)
        elif self.score1_num < self.score2_num:
            self.end_game_screen = End_Game(self.team2.text(), self.score2_num)
        self.end_game_screen.show()
        self.team_in_turn, self.score1_num, self.score2_num = 0, 0, 0
        self.score1.setText(str(self.score1_num))
        self.score2.setText(str(self.score2_num))
        self.endgame.hide()


def window():
    app = QtWidgets.QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    window()
