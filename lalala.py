from playsound import playsound
import threading
import sys
from PyQt5 import QtWidgets
import Clock as clock
import datetime
import pyttsx3
engine = pyttsx3.init()
class ExampleApp(QtWidgets.QMainWindow,clock.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = '00:00:00'
        self.pushButton.clicked.connect(self.knopka)
        threading.Thread(target=self.clock,args=()).start()


    def clock(self):
        while True:
            self.f = str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)
            self.lcdNumber.display(self.f)
    def golos(self):
        engine.say(self.f)
        engine.runAndWait()
    def knopka(self):
        threading.Thread(target=self.golos, args=()).start()








app=QtWidgets.QApplication(sys.argv)
window=ExampleApp()
window.show()
app.exec_()