"""" Игра Крестики-Нолики """
import sys

from PySide6.QtWidgets import QApplication, QWidget

import design

from PySide6.QtCore import QTimer

import random


class TicTacToe(QWidget):
    """" Игровое поле и функции игры"""

    def __init__(self, parent=None):
        super(TicTacToe, self).__init__(parent)
        self.ui = design.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.game_area = [['-', '-', '-'],
                          ['-', '-', '-'],
                          ['-', '-', '-']]
        # индикатор начала игры
        self.game_start = False
        # блокировка поля после хода
        self.player_locked = True
        # количество сделанных ходов
        self.progress = 0
        self.player = 'x'
        self.timer = QTimer(self)
        self.stop_play = False
        self.win_player = None

    def initUI(self):
        button_name = [self.ui.btn_0_0, self.ui.btn_0_1, self.ui.btn_0_2, self.ui.btn_1_0, self.ui.btn_1_1,
                       self.ui.btn_1_2, self.ui.btn_2_0, self.ui.btn_2_1, self.ui.btn_2_2]
        self.config_game_area_buttons()
        self.ui.tabWidget.tabBar().hide()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.btn_x.clicked.connect(lambda: self.set_style_button_selecting(0))
        self.ui.btn_o.clicked.connect(lambda: self.set_style_button_selecting(1))
        self.ui.btn_play.clicked.connect(self.start)
        for btn in button_name:
            btn.clicked.connect(self.on_button_game_area)

    def set_style_button_selecting(self, num):
        """" Устанавливает стиль кнопок выбора символа X или 0 """
        if num == 1:
            self.ui.btn_o.setStyleSheet(u"QPushButton{\n"
                                        "background-color: #000033;\n"
                                        "background-image: url(:/images/resource/images/zero_small.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center center;\n"
                                        "border: 1px solid #333;\n"
                                        "border-left: none;\n"
                                        "border-top-right-radius: 5px;\n"
                                        "border-bottom-right-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "background-color: #000066;\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color: rgb(58, 58, 58);\n"
                                        "}")
            self.ui.btn_x.setStyleSheet(u"QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(45, 45, 45, 255), stop:1 rgba(68, 68, 68, 255));\n"
                                        "background-image: url(:/images/resource/images/cross_small.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center center;\n"
                                        "border: 1px solid #333;\n"
                                        "border-top-left-radius: 5px;\n"
                                        "border-bottom-left-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(66, 66, 66, 255), stop:1 rgba(106, 106, 106, 255));\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color: rgb(58, 58, 58);\n"
                                        "}")
            self.ui.lbl_status.setText('Играешь ноликом')
            self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                             "background: #330066;\n"
                                             "font: 57 16pt \"Roboto Medium\";\n"
                                             "color: white;\n"
                                             "}")
            self.player = '0'
        elif num == 0:
            self.ui.btn_x.setStyleSheet(u"QPushButton{\n"
                                        "background-color: #000033;\n"
                                        "background-image: url(:/images/resource/images/cross_small.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center center;\n"
                                        "border: 1px solid #333;\n"
                                        "border-left: none;\n"
                                        "border-top-left-radius: 5px;\n"
                                        "border-bottom-left-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "background-color: #000066;\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color: rgb(58, 58, 58);\n"
                                        "}")
            self.ui.btn_o.setStyleSheet(u"QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(45, 45, 45, 255), stop:1 rgba(68, 68, 68, 255));\n"
                                        "background-image: url(:/images/resource/images/zero_small.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center center;\n"
                                        "border: 1px solid #333;\n"
                                        "border-top-right-radius: 5px;\n"
                                        "border-bottom-right-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(66, 66, 66, 255), stop:1 rgba(106, 106, 106, 255));\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color: rgb(58, 58, 58);\n"
                                        "}")
            self.ui.lbl_status.setText('Играешь крестиком')
            self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                             "background: #330066;\n"
                                             "font: 57 16pt \"Roboto Medium\";\n"
                                             "color: white;\n"
                                             "}")
            self.player = 'x'

    def set_style_win_cross(self, row, colum):
        """" Стиль для крестика в момент победы"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(0, 170, 0);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(0, 170, 0);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}")

    def set_style_play_cross(self, row, colum):
        """" Стиль для крестика в момент игры"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(37, 35, 49);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(49, 53, 65);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::pressed{\n"
                                                                             "background: rgb(83, 83, 83);\n"
                                                                             "}")

    def set_style_lose_cross(self, row, colum):
        """" Стиль для крестика в момент проигрыша"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(213, 0, 0);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(213, 0, 0);\n"
                                                                             "background-image: url(:/images/resource/images/cross_large.png);\n"
                                                                             "}")

    def set_style_win_zero(self, row, colum):
        """" Стиль для нолика в момент победы"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(0, 170, 0);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(0, 170, 0);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}")

    def set_style_play_zero(self, row, colum):
        """" Стиль для нолика в момент игры"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(37, 35, 49);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(49, 53, 65);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::pressed{\n"
                                                                             "background: rgb(83, 83, 83);\n"
                                                                             "}")

    def set_style_lose_zero(self, row, colum):
        """" Стиль для нолика в момент проигрыша"""
        self.ui.gridLayout.itemAtPosition(row, colum).widget().setStyleSheet(u"QPushButton{\n"
                                                                             "border: none;\n"
                                                                             "background: rgb(213, 0, 0);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}\n"
                                                                             "QPushButton::hover{\n"
                                                                             "background: rgb(213, 0, 0);\n"
                                                                             "background-image: url(:/images/resource/images/zero_large.png);\n"
                                                                             "}")

    def set_area_play(self):
        button_name = [self.ui.btn_0_0, self.ui.btn_0_1, self.ui.btn_0_2, self.ui.btn_1_0, self.ui.btn_1_1,
                       self.ui.btn_1_2, self.ui.btn_2_0, self.ui.btn_2_1, self.ui.btn_2_2]
        for btn in button_name:
            btn.setStyleSheet(u"QPushButton{\n"
                              "border: none;\n"
                              "background: rgb(37, 35, 49);\n"
                              "}\n"
                              "QPushButton::hover{\n"
                              "background: rgb(49, 53, 65);\n"
                              "}\n"
                              "QPushButton::pressed{\n"
                              "background: rgb(83, 83, 83);\n"
                              "}")

    def config_game_area_buttons(self):
        for row in range(0, 3):
            for col in range(0, 3):
                self.ui.gridLayout.itemAtPosition(row, col).widget().setProperty('col', col)
                self.ui.gridLayout.itemAtPosition(row, col).widget().setProperty('row', row)

    def on_button_game_area(self):
        if not self.player_locked:
            button = self.sender()
            row = button.property('row')
            col = button.property('col')
            if self.player == 'x':
                self.set_style_play_cross(row, col)
                self.game_area[row][col] = 'x'
            else:
                self.set_style_play_zero(row, col)
                self.game_area[row][col] = '0'
            self.player_locked = True
            self.progress += 1
            self.check_game_status()
            self.stop_game()
            self.computer_game()

    def lock_player(self):
        if self.player == 'x':
            self.player_locked = False
        else:
            self.player_locked = True

    def start(self):
        """" Устанавливает начальные значения игрового поля и всех переменных """
        if self.game_start:
            self.ui.lbl_status.setText('Поражение!')
            self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                             "background: rgb(213, 0, 0);\n"
                                             "font: 57 16pt \"Roboto Medium\";\n"
                                             "color: white;\n"
                                             "}")
            self.ui.btn_play.setText('Играть')
            self.ui.btn_play.setStyleSheet(u"QPushButton{\n"
                                        "color: white;\n"
                                        "background: none;\n"
                                        "border: none;\n"
                                        "border-radius: 19px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                        "font: 57 16pt \"Roboto Medium\";\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                        "}")
            self.game_start = False
            self.stop_play = True
            self.win_player = None
            self.ui.btn_o.setDisabled(False)
            self.ui.btn_x.setDisabled(False)
            self.player_locked = True
            self.config_game_area_buttons()
            for row in range(0, 3):
                for col in range(0, 3):
                    self.game_area[row][col] = '-'
        else:
            self.config_game_area_buttons()
            for row in range(0, 3):
                for col in range(0, 3):
                    self.game_area[row][col] = '-'
            self.progress = 0
            self.game_start = True
            self.stop_play = False
            self.win_player = '-'
            self.ui.btn_o.setDisabled(True)
            self.ui.btn_x.setDisabled(True)
            self.set_area_play()
            self.lock_player()
            self.ui.lbl_status.setStyleSheet(u"background: none;")
            self.ui.lbl_status.setText('')
            self.ui.btn_play.setText('Сдаться')
            self.ui.btn_play.setStyleSheet(u"QPushButton{\n"
                                           "color: white;\n"
                                           "background: none;\n"
                                           "border: none;\n"
                                           "border-radius: 19px;\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(255, 12, 12, 255), stop:1 rgba(255, 61, 36, 255));\n"
                                           "font: 57 16pt \"Roboto Medium\";\n"
                                           "}\n"
                                           "QPushButton::hover{\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(255, 52, 52, 255), stop:1 rgba(255, 93, 72, 255));\n"
                                           "}\n"
                                           "QPushButton::pressed{\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                           "}")
        if self.player != 'x':
            self.computer_game()

    def computer_game(self):
        n = random.randint(0, 3)
        comp_answer = ['Думаю...', 'Мой ход', 'Так так так...', 'Сложно...']
        if self.stop_play:
            return
        else:
            self.ui.lbl_status.setText(comp_answer[n])
            self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                         "background: #330066;\n"
                                         "font: 57 16pt \"Roboto Medium\";\n"
                                         "color: white;\n"
                                         "}")
            self.timer.singleShot(2000, self.computer_move)

    def computer_move(self):
        if self.player == 'x':
            comp = '0'
        else:
            comp = 'x'
        self.timer.stop()
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.game_area[row][col] == '-':
                self.game_area[row][col] = comp
                if comp == 'x':
                    self.set_style_play_cross(row, col)
                    self.progress += 1
                    self.check_game_status()
                    self.stop_game()
                    self.player_locked = False
                else:
                    self.set_style_play_zero(row, col)
                    self.progress += 1
                    self.check_game_status()
                    self.stop_game()
                    self.player_locked = False
                break
            self.ui.lbl_status.setText('Твой ход')
            self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                                 "background: #330066;\n"
                                                 "font: 57 16pt \"Roboto Medium\";\n"
                                                 "color: white;\n"
                                                 "}")

    def check_game_status(self):
        self.win_player = '-'
        list_player = ['x', '0']
        # проверка строк на выигрышную комбинацию
        for i in range(0, 2):
            for row in range(0, 3):
                if self.game_area[row][0] == list_player[i] and self.game_area[row][1] == list_player[i] and self.game_area[row][2] == list_player[i]:
                    self.stop_play = True
                    self.win_player = list_player[i]
                    if self.win_player == self.player:
                        if self.player == 'x':
                            self.set_style_win_cross(row, 0)
                            self.set_style_win_cross(row, 1)
                            self.set_style_win_cross(row, 2)
                        else:
                            self.set_style_win_zero(row, 0)
                            self.set_style_win_zero(row, 1)
                            self.set_style_win_zero(row, 2)
                    else:
                        if self.player == 'x':
                            self.set_style_lose_zero(row, 0)
                            self.set_style_lose_zero(row, 1)
                            self.set_style_lose_zero(row, 2)
                        else:
                            self.set_style_lose_cross(row, 0)
                            self.set_style_lose_cross(row, 1)
                            self.set_style_lose_cross(row, 2)
                    return
        # проверка столбцов
            for col in range(0, 3):
                if self.game_area[0][col] == list_player[i] and self.game_area[1][col] == list_player[i] and self.game_area[2][col] == list_player[i]:
                    self.stop_play = True
                    self.win_player = list_player[i]
                    if self.win_player == self.player:
                        if self.player == 'x':
                            self.set_style_win_cross(0, col)
                            self.set_style_win_cross(1, col)
                            self.set_style_win_cross(2, col)
                        else:
                            self.set_style_win_zero(0, col)
                            self.set_style_win_zero(1, col)
                            self.set_style_win_zero(2, col)
                    else:
                        if self.player == 'x':
                            self.set_style_lose_zero(0, col)
                            self.set_style_lose_zero(1, col)
                            self.set_style_lose_zero(2, col)
                        else:
                            self.set_style_lose_cross(0,col)
                            self.set_style_lose_cross(1, col)
                            self.set_style_lose_cross(2, col)
                    return
        # проверка диагоналей
            if self.game_area[0][0] == list_player[i] and self.game_area[1][1] == list_player[i] and self.game_area[2][2] == list_player[i]:
                self.stop_play = True
                self.win_player = list_player[i]
                if self.win_player == self.player:
                    if self.player == 'x':
                        self.set_style_win_cross(0, 0)
                        self.set_style_win_cross(1, 1)
                        self.set_style_win_cross(2, 2)
                    else:
                        self.set_style_win_zero(0, 0)
                        self.set_style_win_zero(1, 1)
                        self.set_style_win_zero(2, 2)
                else:
                    if self.player == 'x':
                        self.set_style_lose_zero(0, 0)
                        self.set_style_lose_zero(1, 1)
                        self.set_style_lose_zero(2, 2)
                    else:
                        self.set_style_lose_cross(0, 0)
                        self.set_style_lose_cross(1, 1)
                        self.set_style_lose_cross(2, 2)
                return
            if self.game_area[0][2] == list_player[i] and self.game_area[1][1] == list_player[i] and self.game_area[2][0] == list_player[i]:
                self.stop_play = True
                self.win_player = list_player[i]
                if self.win_player == self.player:
                    if self.player == 'x':
                        self.set_style_win_cross(0, 2)
                        self.set_style_win_cross(1, 1)
                        self.set_style_win_cross(2, 0)
                    else:
                        self.set_style_win_zero(0, 2)
                        self.set_style_win_zero(1, 1)
                        self.set_style_win_zero(2, 0)
                else:
                    if self.player == 'x':
                        self.set_style_lose_zero(0, 2)
                        self.set_style_lose_zero(1, 1)
                        self.set_style_lose_zero(2, 0)
                    else:
                        self.set_style_lose_cross(0, 2)
                        self.set_style_lose_cross(1, 1)
                        self.set_style_lose_cross(2, 0)
                return
        if self.progress == 9:
            self.stop_play = True

    def stop_game(self):
        if self.stop_play:
            if self.win_player == self.player:
                self.ui.lbl_status.setText('Победа!')
                self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                                 "background: rgb(0, 170, 0);\n"
                                                 "font: 57 16pt \"Roboto Medium\";\n"
                                                 "color: white;\n"
                                                 "}")
                self.ui.btn_play.setText('Играть')
                self.ui.btn_play.setStyleSheet(u"QPushButton{\n"
                                               "color: white;\n"
                                               "background: none;\n"
                                               "border: none;\n"
                                               "border-radius: 19px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                               "font: 57 16pt \"Roboto Medium\";\n"
                                               "}\n"
                                               "QPushButton::hover{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                               "}\n"
                                               "QPushButton::pressed{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                               "}")
                self.game_start = False
                self.stop_play = True
                self.ui.btn_o.setDisabled(False)
                self.ui.btn_x.setDisabled(False)
                self.player_locked = True
            elif self.win_player == '-':
                self.ui.lbl_status.setText('Ничья')
                self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                                 "background: #330066;\n"
                                                 "font: 57 16pt \"Roboto Medium\";\n"
                                                 "color: white;\n"
                                                 "}")
                self.ui.btn_play.setText('Играть')
                self.ui.btn_play.setStyleSheet(u"QPushButton{\n"
                                               "color: white;\n"
                                               "background: none;\n"
                                               "border: none;\n"
                                               "border-radius: 19px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                               "font: 57 16pt \"Roboto Medium\";\n"
                                               "}\n"
                                               "QPushButton::hover{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                               "}\n"
                                               "QPushButton::pressed{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                               "}")
                self.game_start = False
                self.stop_play = True
                self.ui.btn_o.setDisabled(False)
                self.ui.btn_x.setDisabled(False)
                self.player_locked = True
            else:
                self.ui.lbl_status.setText('Проиграл')
                self.ui.lbl_status.setStyleSheet(u"QLabel{\n"
                                                 "background: rgb(213, 0, 0);\n"
                                                 "font: 57 16pt \"Roboto Medium\";\n"
                                                 "color: white;\n"
                                                 "}")
                self.ui.btn_play.setText('Играть')
                self.ui.btn_play.setStyleSheet(u"QPushButton{\n"
                                               "color: white;\n"
                                               "background: none;\n"
                                               "border: none;\n"
                                               "border-radius: 19px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(43, 54, 232, 255), stop:1 rgba(0, 108, 237, 255));\n"
                                               "font: 57 16pt \"Roboto Medium\";\n"
                                               "}\n"
                                               "QPushButton::hover{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(83, 92, 232, 255), stop:1 rgba(75, 149, 237, 255));\n"
                                               "}\n"
                                               "QPushButton::pressed{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.0172273, y1:0.023, x2:0.0227273, y2:1, stop:0.170455 rgba(14, 27, 232, 255), stop:1 rgba(49, 98, 156, 255));\n"
                                               "}")
                self.game_start = False
                self.stop_play = True
                self.ui.btn_o.setDisabled(False)
                self.ui.btn_x.setDisabled(False)
                self.player_locked = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
