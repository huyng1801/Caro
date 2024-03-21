import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtMultimedia import*
from PyQt5.QtMultimediaWidgets import*
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createVideoBackGround()
        self.createMenuInterface()
        self.inputPlayer()
        self.createGameInterface()
        self.createBoard()
        self.loopVideoBackground()
        self.createSound()
        self.createPushButtonMove()
        self.diagonal()
        
        
    def createVideoBackGround(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.QVWVideoBackGround = QVideoWidget(self)
        self.QVWVideoBackGround.setGeometry(0, 0, 1920, 1080)
        self.videoPlayer = QMediaPlayer()
        self.videoPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("video\\background.mp4")))
        self.videoPlayer.setVideoOutput(self.QVWVideoBackGround)
        self.videoPlayer.positionChanged.connect(lambda: self.loopVideoBackground())
        self.videoPlayer.play()
        self.QSW = QStackedWidget(self)
        self.QSW.setGeometry(210, 162, 1516, 762)
    def createMenuInterface(self):
        self.QWMenu = QWidget()
        self.QWMenu.setGeometry(0, 0, 1516, 762)
        self.QWMenu.setObjectName("QWMenu")
        self.QWMenu.setStyleSheet("QWidget#QWMenu{background-color: rgb(30, 30, 30);}"
                                  "QPushButton{color: rgb(248, 248, 242); border-radius: 30px; height: 60px; font: 18pt; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 130, 255, 255), stop:0.985075 rgba(255, 55, 0, 255), stop:1 rgba(255, 255, 255, 255));}"
                                  "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.199005 rgba(0, 130, 255, 255), stop:0.985075 rgba(255, 55, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.QLBackgroundMenu = QLabel(self.QWMenu)
        self.QLBackgroundMenu.setGeometry(0, 0, 1516, 762)
        self.QLBackgroundMenu.setPixmap(QPixmap("icon\\backgroundmenu.jpg"))
        self.QLBackgroundMenu.setScaledContents(True)
        self.verticalLayoutWidget = QWidget(self.QWMenu)
        self.verticalLayoutWidget.setGeometry(QRect(578, 180, 360, 450))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.QVBLMenu = QVBoxLayout(self.verticalLayoutWidget)
        self.QVBLMenu.setContentsMargins(0, 0, 0, 0)
        self.QVBLMenu.setSpacing(0)

        self.QPBNewGame = QPushButton(self.verticalLayoutWidget)
        self.QPBNewGame.setText("Trò chơi mới")
        self.QPBNewGame.clicked.connect(lambda: self.QSW.setCurrentIndex(1))
        self.QPBMusic = QPushButton(self.verticalLayoutWidget)
        self.QPBMusic.setText("Âm nhạc: Bật")
        self.QPBMusic.clicked.connect(lambda: self.onOffMusic())
        self.QPBEffect = QPushButton(self.verticalLayoutWidget)
        self.QPBEffect.setText("Hiệu ứng: Bật")
        self.QPBEffect.clicked.connect(lambda: self.onOffEffect())
        self.QPBExit = QPushButton(self.verticalLayoutWidget)
        self.QPBExit.setText("Thoát")
        self.QPBExit.clicked.connect(lambda: main_win.close())
        self.QVBLMenu.addWidget(self.QPBNewGame)
        self.QVBLMenu.addWidget(self.QPBMusic)
        self.QVBLMenu.addWidget(self.QPBEffect)
        self.QVBLMenu.addWidget(self.QPBExit)
        self.QSW.addWidget(self.QWMenu)
    def onOffMusic(self):
        if self.QPBMusic.text() == "Âm nhạc: Bật":
            self.soundGame.setMuted(True)
            self.QPBMusic.setText("Âm nhạc: Tắt")
        elif self.QPBMusic.text() == "Âm nhạc: Tắt":
            self.soundGame.setMuted(False)
            self.QPBMusic.setText("Âm nhạc: Bật")
    def onOffEffect(self):
        if self.QPBEffect.text() == "Hiệu ứng: Bật":
            self.soundMove.setMuted(True)
            self.soundTick.setMuted(True)
            self.soundVictory.setMuted(True)
            self.QPBEffect.setText("Hiệu ứng: Tắt")
        elif self.QPBEffect.text() == "Hiệu ứng: Tắt":
            self.soundMove.setMuted(False)
            self.soundTick.setMuted(False)
            self.soundVictory.setMuted(False)
            self.QPBEffect.setText("Hiệu ứng: Bật")
    def inputPlayer(self):
        self.QWInputPlayer = QWidget()
        self.QWInputPlayer.setGeometry(0, 0, 1516, 762)
        self.QWInputPlayer.setStyleSheet("QWidget{background-color: rgb(30, 30, 30);}"
                        "QLabel{background-color: rgba(255, 255, 255, 0); color: rgb(248, 248, 242); font: 16pt;}"
                        "QPushButton{color: rgb(248, 248, 242); border-radius: 25px; font: 16pt; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 130, 255, 255), stop:0.985075 rgba(255, 55, 0, 255), stop:1 rgba(255, 255, 255, 255));}"
                                  "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.199005 rgba(0, 130, 255, 255), stop:0.985075 rgba(255, 55, 0, 255), stop:1 rgba(255, 255, 255, 255));}"
                        "QLabel{background-color: rgba(0, 0, 0, 0); color: rgb(248, 248, 242); font: 16pt;}"
                        "QLineEdit{background-color: rgba(248, 248, 242, 0); font: 16pt; color: rgb(248, 248, 242); border: none; border-bottom: 2px solid rgb(248, 248, 242);}"
                        "QLineEdit:focus{background-color: rgba(248, 248, 242, 100); border: 2px solid rgb(248, 248, 242);  border-radius: 5px;}")
        self.QLBackgroundInputPlayer = QLabel(self.QWInputPlayer)
        self.QLBackgroundInputPlayer.setGeometry(0, 0, 1516, 762)
        self.QLBackgroundInputPlayer.setPixmap(QPixmap("icon\\backgroundmenu.jpg"))
        self.QLBackgroundInputPlayer.setScaledContents(True)
        self.QLNamePlayer1 = QLabel(self.QWInputPlayer)
        self.QLNamePlayer1.setGeometry(558, 180, 500, 50)
        self.QLNamePlayer1.setText("Tên người chơi 1:")
        self.QLNamePlayer2 = QLabel(self.QWInputPlayer)
        self.QLNamePlayer2.setGeometry(558, 380, 500, 50)
        self.QLNamePlayer2.setText("Tên người chơi 2:")
        self.QLENamePlayer1 = QLineEdit(self.QWInputPlayer)
        self.QLENamePlayer1.setGeometry(558, 250, 400, 50)
        self.QLENamePlayer1.setPlaceholderText("Nhập tên người chơi 1")
        self.QLENamePlayer2 = QLineEdit(self.QWInputPlayer)
        self.QLENamePlayer2.setGeometry(558, 450, 400, 50)
        self.QLENamePlayer2.setPlaceholderText("Nhập tên người chơi 2")
        self.QPBAgree = QPushButton(self.QWInputPlayer)
        self.QPBAgree.setGeometry(1258, 680, 200, 50)
        self.QPBAgree.setText("Đồng ý")
        self.QPBAgree.clicked.connect(lambda: self.loadGame())
        self.QPBBack = QPushButton(self.QWInputPlayer)
        self.QPBBack.setGeometry(58, 680, 200, 50)
        self.QPBBack.setText("Trở về")
        self.QPBBack.clicked.connect(lambda: self.QSW.setCurrentIndex(0))
        self.QSW.addWidget(self.QWInputPlayer)
    def loadGame(self):
        self.QSW.setCurrentIndex(2)
        self.QLPlayer1.setText(self.QLENamePlayer1.text())
        self.QLPlayer2.setText(self.QLENamePlayer2.text())
    def createGameInterface(self):
        self.QWGame = QWidget()
        self.QWGame.setGeometry(0, 0, 1516, 762)
        self.QWGame.setStyleSheet("QWidget{background-color: rgb(0, 0, 0);}"
                        "QLabel{background-color: rgba(255, 255, 255, 0); color: red; font: 16pt;}"
                        "QPushButton{font-weight: bold; border-radius: 5px; background-color: rgb(68, 71, 90); font: 12pt; color: rgb(248, 248, 242)}"
                        "QPushButton{font-weight: bold; background-color: rgb(68, 71, 90); font: 12pt;}")
        self.QWBoard = QWidget(self.QWGame)
        self.QWBoard.setGeometry(379, 2, 758, 758)
        self.QFBoard = QFrame(self.QWBoard)
        self.QFBoard.setGeometry(-1, -1, 770, 770)

        self.QLPlayer1 = QLabel(self.QWGame)
        self.QLPlayer1.setGeometry(0, 50, 373, 100)
        self.QLPlayer1.setText(self.QLENamePlayer1.text())
        self.QLPlayer1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.QLPlayer1.setStyleSheet("QLabel{background-color: rgba(255, 255, 255, 0); color: blue; font: 16pt;}")
        self.QLPlayer2 = QLabel(self.QWGame)
        self.QLPlayer2.setGeometry(1143, 50, 373, 100)
        self.QLPlayer2.setText(self.QLENamePlayer2.text())
        self.QLPlayer2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.QLO = QLabel(self.QWGame)
        self.QLO.setGeometry(80, 170, 200, 200)
        self.QLO.setPixmap(QPixmap("icon\\o.png"))
        self.QLO.setScaledContents(True)
        self.QLX = QLabel(self.QWGame)
        self.QLX.setGeometry(1230, 170, 200, 200)
        self.QLX.setPixmap(QPixmap("icon\\x.png"))
        self.QLX.setScaledContents(True)
        self.QPBReplay = QPushButton(self.QWGame)
        self.QPBReplay.setGeometry(1225, 675, 210, 60)
        self.QPBReplay.setText("Chơi lại")
        self.QPBReplay.clicked.connect(lambda: self.replay())
        self.QPBReplay.setAutoDefault(False)
        self.QPBReplay.setDefault(False)
        self.QPBReplay.setFlat(False)
        self.QPBReplay.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBReplay.setShortcut("R")
        self.QLWinner = QLabel(self.QWBoard)
        self.QLWinner.setGeometry(0, 0, 758, 758)
        self.QLWinner.hide()
        self.QLWinner.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.QLWinner.setStyleSheet("QLabel{background-color: rgba(255, 255, 255, 0); color: yellow; font: 36pt; font-weight: bold;}")
        self.QSW.addWidget(self.QWGame)
    def loopVideoBackground(self):
        if self.videoPlayer.duration() == self.videoPlayer.position():
            self.videoPlayer.setPosition(0)
            self.videoPlayer.play()
    def createBoard(self):
        self.player = "O"
        self.listPushButton = []
        for i in range(19):
            temp = []
            for j in range(19):
                temp.append(QPushButton(self.QFBoard))
            self.listPushButton.append(temp)
        for i in range(19):
            for j in range(19):
                self.listPushButton[i][j].setGeometry(40*i, 40*j, 40, 40)
                self.listPushButton[i][j].clicked.connect(lambda: self.tick())
                self.listPushButton[i][j].setText("")
                self.listPushButton[i][j].setAutoDefault(True)
                self.listPushButton[i][j].setDefault(True)
                self.listPushButton[i][j].setFlat(True)
                self.listPushButton[i][j].setStyleSheet("QPushButton{background-color: rgba(248, 248, 242, 0); border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                            "QPushButton:focus{background-color: rgba(98, 114, 164, 150);}")
    def diagonal(self):
        self.listDiagonal = []
        for i in range(4, 19):
            j = 18
            temp = []
            while i != -1 and j != -1:
                temp.append(self.listPushButton[i][j])
                i -= 1
                j -= 1
            self.listDiagonal.append(temp)
        for j in range(4, 18):
            i = 18
            temp = []
            while i != -1 and j != -1:
                temp.append(self.listPushButton[i][j])
                i -= 1
                j -= 1
            self.listDiagonal.append(temp)
        for i in range(4, 19):
            j = 0
            temp = []
            while i != -1 and j != 19:
                temp.append(self.listPushButton[i][j])
                i -= 1
                j += 1
            
            self.listDiagonal.append(temp)
        for j in range(1, 15):
            i = 18
            temp = []
            while i != -1 and j != 19:
                temp.append(self.listPushButton[i][j])
                i -= 1
                j += 1
            self.listDiagonal.append(temp)
        self.listPushButton[9][9].setFocus()
    def createSound(self):
        self.url = QUrl.fromLocalFile("sound\\tick.mp3")
        self.content = QMediaContent(self.url)
        self.soundTick = QMediaPlayer()
        self.soundTick.setMedia(self.content)
        self.soundTick.setVolume(40)
        self.url2 = QUrl.fromLocalFile("sound\\move.mp3")
        self.content2 = QMediaContent(self.url2)
        self.soundMove = QMediaPlayer()
        self.soundMove.setVolume(20)
        self.soundMove.setMedia(self.content2)
        self.url3 = QUrl.fromLocalFile("sound\\victory.mp3")
        self.content3 = QMediaContent(self.url3)
        self.soundVictory = QMediaPlayer()
        self.soundVictory.setMedia(self.content3)
        self.url4 = QUrl.fromLocalFile("sound\\game.mp3")
        self.content4 = QMediaContent(self.url4)
        self.soundGame = QMediaPlayer()
        self.soundGame.setMedia(self.content4)
        self.soundGame.positionChanged.connect(lambda: self.loopSoundGame())
        self.soundGame.play()
    def loopSoundGame(self):
        if self.soundGame.position() == self.soundGame.duration():
            self.soundGame.setPosition(0)
            self.soundGame.play()
    def createPushButtonMove(self):
        self.QPBKeyLeft = QPushButton(self.QWGame)
        self.QPBKeyLeft.setGeometry(1225, 500, 60, 60)
        self.QPBKeyLeft.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyLeft.setShortcut("Left")
        self.QPBKeyLeft.setIcon(QIcon("icon\\keyleft.png"))
        self.QPBKeyLeft.setIconSize(QSize(30, 30))
        self.QPBKeyLeft.setObjectName("QPBKeyLeft")
        self.QPBKeyLeft.clicked.connect(lambda: self.move())
        self.QPBKeyRight = QPushButton(self.QWGame)
        self.QPBKeyRight.setGeometry(1375, 500, 60, 60)
        self.QPBKeyRight.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyRight.setShortcut("Right")
        self.QPBKeyRight.setIcon(QIcon("icon\\keyright.png"))
        self.QPBKeyRight.setIconSize(QSize(30, 30))
        self.QPBKeyRight.setObjectName("QPBKeyRight")
        self.QPBKeyRight.clicked.connect(lambda: self.move())
        self.QPBKeyUp = QPushButton(self.QWGame)
        self.QPBKeyUp.setGeometry(1300, 425, 60, 60)
        self.QPBKeyUp.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyUp.setShortcut("Up")
        self.QPBKeyUp.setIcon(QIcon("icon\\keyup.png"))
        self.QPBKeyUp.setIconSize(QSize(30, 30))
        self.QPBKeyUp.setObjectName("QPBKeyUp")
        self.QPBKeyUp.clicked.connect(lambda: self.move())
        self.QPBKeyDown = QPushButton(self.QWGame)
        self.QPBKeyDown.setGeometry(1300, 500, 60, 60)
        self.QPBKeyDown.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyDown.setShortcut("Down")
        self.QPBKeyDown.setIcon(QIcon("icon\\keydown.png"))
        self.QPBKeyDown.setIconSize(QSize(30, 30))
        self.QPBKeyDown.setObjectName("QPBKeyDown")
        self.QPBKeyDown.clicked.connect(lambda: self.move())
        self.QPBKeyA = QPushButton(self.QWGame)
        self.QPBKeyA.setGeometry(75, 500, 60, 60)
        self.QPBKeyA.setText("A")
        self.QPBKeyA.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyA.setShortcut("A")
        self.QPBKeyA.clicked.connect(lambda: self.move())
        self.QPBKeyD = QPushButton(self.QWGame)
        self.QPBKeyD.setGeometry(225, 500, 60, 60)
        self.QPBKeyD.setText("D")
        self.QPBKeyD.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyD.setShortcut("D")
        self.QPBKeyD.clicked.connect(lambda: self.move())
        self.QPBKeyW = QPushButton(self.QWGame)
        self.QPBKeyW.setGeometry(150, 425, 60, 60)
        self.QPBKeyW.setText("W")
        self.QPBKeyW.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyW.setShortcut("W")
        self.QPBKeyW.clicked.connect(lambda: self.move())
        self.QPBKeyS = QPushButton(self.QWGame)
        self.QPBKeyS.setGeometry(150, 500, 60, 60)
        self.QPBKeyS.setText("S")
        self.QPBKeyS.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyS.setShortcut("S")
        self.QPBKeyS.clicked.connect(lambda: self.move())
        self.QPBKeySpace = QPushButton(self.QWGame)
        self.QPBKeySpace.setGeometry(75, 600, 210, 60)
        self.QPBKeySpace.setText("Space")
        self.QPBKeySpace.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QPBKeyBackspace = QPushButton(self.QWGame)
        self.QPBKeyBackspace.setGeometry(75, 675, 210, 60)
        self.QPBKeyBackspace.setText("Trở về")
        self.QPBKeyBackspace.setShortcut("Backspace")
        self.QPBKeyBackspace.clicked.connect(lambda: self.QSW.setCurrentIndex(1))
        self.QPBKeyEnter = QPushButton(self.QWGame)
        self.QPBKeyEnter.setGeometry(1225, 600, 210, 60)
        self.QPBKeyEnter.setText("Enter")
        self.QPBKeyEnter.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    def replay(self):
        self.QLWinner.hide()
        self.player = "O"
        for i in range(19):
            for j in range(19):
                self.listPushButton[i][j].setText("")
                self.listPushButton[i][j].setEnabled(True)
                self.listPushButton[9][9].setFocus()
                self.listPushButton[i][j].setStyleSheet("QPushButton{background-color: rgba(248, 248, 242, 0); border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                        "QPushButton:focus{background-color: rgb(98, 114, 164);}")
    def keyPressEvent(self, e: QKeyEvent) -> None:
        if (e.key() == Qt.Key.Key_Escape):
            main_win.close()
    def move(self):
        self.soundMove.setPosition(0)
        self.soundMove.play()
        for i in range(19):
            for j in range(19):
                if self.listPushButton[i][j].hasFocus():
                    if self.sender().objectName() == "QPBKeyLeft" or self.sender().text() == "A":
                        self.listPushButton[(i-1)%19][j].setFocus()
                        return
                    elif self.sender().objectName() == "QPBKeyRight" or self.sender().text() == "D":
                        self.listPushButton[(i+1)%19][j].setFocus()
                        return
                    elif self.sender().objectName() == "QPBKeyUp" or self.sender().text() == "W":
                        self.listPushButton[i][(j-1)%19].setFocus()
                        return
                    elif self.sender().objectName() == "QPBKeyDown" or self.sender().text() == "S":
                        self.listPushButton[i][(j+1)%19].setFocus()
                        return
    def tick(self):
        self.soundTick.setPosition(0)
        self.soundTick.play()
        if self.sender().text() == "":
            if self.player == "O":
                self.sender().setText(self.player)
                self.player = "X"
                self.sender().setStyleSheet("QPushButton{background-color: rgba(248, 248, 242, 0); color: rgb(0, 0, 255);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                        "QPushButton:focus{background-color: rgb(98, 114, 164);}")
            elif self.player == "X":
                self.sender().setText(self.player)
                self.player = "O"
                self.sender().setStyleSheet("QPushButton{background-color: rgba(248, 248, 242, 0); color: rgb(255, 0, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"                                "QPushButton:focus{background-color: rgb(98, 114, 164);}")
        self.checkWinner()
    def setDisableBoard(self):
        for i in range(19):
            for j in range(19):
                self.listPushButton[i][j].setDisabled(True)          
    def checkWinner(self):
        for i in range(19):
            for j in range(15):
                if (self.listPushButton[i][j].text() == "O" and self.listPushButton[i][j+1].text() == "O"
                    and self.listPushButton[i][j+2].text() == "O" and self.listPushButton[i][j+3].text() == "O" and self.listPushButton[i][j+4].text() == "O"):
                        self.QLWinner.setText(f"{self.QLENamePlayer1.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        for k in range(5):
                            self.listPushButton[i][j+k].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);;border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
                elif (self.listPushButton[i][j].text() == "X" and self.listPushButton[i][j+1].text() == "X"
                    and self.listPushButton[i][j+2].text() == "X" and self.listPushButton[i][j+3].text() == "X" and self.listPushButton[i][j+4].text() == "X"):
                        self.QLWinner.setText(f"{self.QLENamePlayer2.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        for k in range(5):
                            self.listPushButton[i][j+k].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
        for j in range(19):
            for i in range(15):
                if (self.listPushButton[i][j].text() == "O" and self.listPushButton[i+1][j].text() == "O"
                    and self.listPushButton[i+2][j].text() == "O" and self.listPushButton[i+3][j].text() == "O" and self.listPushButton[i+4][j].text() == "O"):
                        self.QLWinner.setText(f"{self.QLENamePlayer1.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        for k in range(5):
                            self.listPushButton[i+k][j].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);;border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
                elif (self.listPushButton[i][j].text() == "X" and self.listPushButton[i+1][j].text() == "X"
                    and self.listPushButton[i+2][j].text() == "X" and self.listPushButton[i+3][j].text() == "X" and self.listPushButton[i+4][j].text() == "X"):
                        self.QLWinner.setText(f"{self.QLENamePlayer2.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        for k in range(5):
                            self.listPushButton[i+k][j].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
        for i in range(len(self.listDiagonal)):
            for j in range((len(self.listDiagonal[i])-4)):
                if (j + 4 < len(self.listDiagonal[i]) and self.listDiagonal[i][j].text() == "O" and self.listDiagonal[i][j+1].text() == "O"
                    and self.listDiagonal[i][j+2].text() == "O" and self.listDiagonal[i][j+3].text() == "O" and self.listDiagonal[i][j+4].text() == "O"):
                        self.QLWinner.setText(f"{self.QLENamePlayer1.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        self.listDiagonal[i][j].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+1].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+2].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+3].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+4].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(0, 255, 0);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
                elif (j + 4 < len(self.listDiagonal[i]) and self.listDiagonal[i][j].text() == "X" and self.listDiagonal[i][j+1].text() == "X"
                    and self.listDiagonal[i][j+2].text() == "X" and self.listDiagonal[i][j+3].text() == "X" and self.listDiagonal[i][j+4].text() == "X"):
                        self.QLWinner.setText(f"{self.QLENamePlayer2.text()}\n\n đã giành chiến thắng")
                        self.QLWinner.show()
                        self.soundVictory.play()
                        self.listDiagonal[i][j].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+1].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+2].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+3].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.listDiagonal[i][j+4].setStyleSheet("QPushButton{background-color: rgb(241, 250, 140); color: rgb(255, 85, 85);border: 1px solid rgb(248, 248, 242); font: 24pt 'MS Shell Dlg 2'; font-weight: bold;}"
                                                       "QPushButton:focus{background-color: rgb(98, 114, 164);}")
                        self.setDisableBoard()
                        return
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    sys.exit(app.exec())   