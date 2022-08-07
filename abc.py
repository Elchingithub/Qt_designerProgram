from PyQt5.QtWidgets import *
import sqlite3 
from resume import Ui_Form
import random
import time
print(random.randint(100000, 999999))
print("Ekrandaki kodu Password bolmesine daxil edin")
time.sleep(1.5)
class register(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add)
        
    def add(self):
        par = "INSERT INTO MAIl Values(?,?)"
        Gmail = self.ui.textEdit.toPlainText()
        Password = self.ui.textEdit_2.toPlainText()
        Your_resume = self.ui.textEdit_3.toPlainText()
        co = sqlite3.connect('database')
        co.execute('CREATE TABLE IF NOT EXISTS MAIl(GMAIL TEXT NOT NULL UNIQUE, PASSWORD INT)')
        co.execute(par, (Gmail,Password,))
        co.commit()
        co.close()
        with open('resume.txt', 'a+', encoding = 'UTF-8') as file:
            file.write(Your_resume)

alp = QApplication([])
window = register()
window.show()
alp.exec_()
