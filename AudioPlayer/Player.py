import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class AudioPlayer(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400, 300)

        place = self.frameGeometry()
        centre = QDesktopWidget().availableGeometry().center()
        place.moveCenter(centre)
        self.move(place.topLeft())

        self.videowidget = QVideoWidget()
        self.player = QMediaPlayer()

        self.layout = QVBoxLayout()
        self.layout.addStretch(1)
        self.setLayout(self.layout)


        self.time = QHBoxLayout()

        self.startTimeLabel = QLabel('00:00')
        self.endTimeLabel = QLabel('00:00')



        self.sldPosition = QSlider(Qt.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.sliderMoved[int].connect(self.position)
        self.layout.addWidget(self.sldPosition)

        self.time.addWidget(self.startTimeLabel)
        self.time.addWidget(self.endTimeLabel)

        self.layout.addLayout(self.time)


        self.player.positionChanged.connect(self.sldPosition.setValue)

        self.player.durationChanged.connect(self.duration)

        self.sldPosition.setEnabled(False)

        self.btnplay = QPushButton(" ▶️", clicked=self.play)
        self.layout.addWidget(self.btnplay)
        self.btnplay.setFixedSize(40, 40)
        self.btnplay.setEnabled(False)


        self.btnpause = QPushButton("||", clicked=self.pause)
        self.layout.addWidget(self.btnpause)
        self.btnpause.setFixedSize(40, 40)
        self.btnpause.setEnabled(False)


        volumeControl = QHBoxLayout()
        self.layout.addLayout(volumeControl)

        btnVolumeUp = QPushButton('+', clicked=self.volumeUp)
        btnVolumeDown = QPushButton('-', clicked=self.volumeDown)
        butVolumeMute = QPushButton('Mute', clicked=self.volumeMute)
        volumeControl.addWidget(btnVolumeUp)
        volumeControl.addWidget(butVolumeMute)
        volumeControl.addWidget(btnVolumeDown)

        findAudio = QHBoxLayout()
        self.layout.addLayout(findAudio)

        btnOpenFile = QPushButton('Open', clicked=self.OpenAudioFile)
        findAudio.addWidget(btnOpenFile)

        self.player.error.connect(self._errorHandle)

    def position(self, value):
         self.player.setPosition(value)

    def duration(self, t):
        self.sldPosition.setRange(0, t)
        self.startTimeLabel.setText('00:00')

    def pause(self):
        try:
            self.player.pause()
            self.btnplay.setEnabled(True)
            self.btnpause.setEnabled(False)
        except:
            return

    def play(self):
        try:
            self.player.play()
            self.btnpause.setEnabled(True)
            self.btnplay.setEnabled(False)
        except:
            return

    def volumeUp(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def OpenAudioFile(self):

        findFile = QFileDialog.getOpenFileName(self)

        if findFile != '':
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(findFile[0])))
            self.player.play()
            self.btnpause.setEnabled(True)
            self.sldPosition.setEnabled(True)
        else:
            return

    def _errorHandle(self, error):
        print('ERROR', error, self.player.errorString())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    App = AudioPlayer()
    App.show()
    sys.exit(app.exec_())