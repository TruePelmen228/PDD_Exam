import sys
import headder
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import  QDialog, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QPushButton, QLabel, QCheckBox
from PyQt6.QtCore import QTimer





def word_wrap(x):
    
    s=x.text()
    i=0
    while i<len(s):
        if i>0 and i%(500//6)==0:
            k=i
            while s[k]!=' ':
                k-=1
            s=s[:k:]+'\n'+s[k::]
            i+=1
        i+=1
    x.setText(s)   
class MainWindow(QMainWindow):
    h=[]
    queue_q=headder.take_five('дорожные знаки', h)+headder.take_five('остановка и стоянка', h)+headder.take_five('общие положения', h)
    start_wd=[]
    big_queue=[]
    ans_q=[]
    tabel=[]
    g=0
    def __init__(self):
        super().__init__()

        #create a window
        self.setWindowTitle("Экзамен по ПДД")
        self.resize(785, 600)
        fff=open('ui_ss.qss.py' , 'r')
        style=fff.read()
        self.setStyleSheet(style)
        self.timer=QLabel()
        self.timer.resize(300, 40)
        self.timer.hide()
        button_st = QPushButton("Начать экзамен", self)
        button_st.setCheckable(True)
        button_st.resize(150, 80)
        button_st.clicked.connect(self.exam)
        button_st.move(590,500)
        button_st1 = QPushButton("Посмотреть статистику", self)
        button_st1.setCheckable(True)
        button_st1.resize(200, 80)
        #button_st1.clicked.connect(self.exam)
        button_st1.move(580,400)
        self.start_wd.append(button_st1)
        
        
    def exam(self):
        
        self.sender().hide()
        self.start_wd[0].hide()
        for i in range(len(self.queue_q)):
                masas=[]           
                label = QLabel(self.queue_q[self.g+i][2], self)
                lb = QLabel(self)
                label.setWordWrap(True)
                label.resize(785, 100)
                #print(str(self.queue_q[self.g+i][3]))
                if str(self.queue_q[self.g+i][3])!='-':
                    print(str(self.queue_q[self.g+i][3]))
                    lb.setPixmap(QPixmap(str(self.queue_q[self.g+i][3])))
                    lb.move(65, 110)
                    lb.resize(645, 250)
                #self.setCentralWidget(lb)
                #self.resize(image.width(), image.height())
                label.hide()
                lb.hide()
                masas.append(label)
                masas.append(lb)
                a1 =QCheckBox(self)
                a2 =QCheckBox(self)
                a3 =QCheckBox(self)
                ot=50
                a1.stateChanged.connect(self.onStateChanged)
                a2.stateChanged.connect(self.onStateChanged)
                a3.stateChanged.connect(self.onStateChanged)
                sas=[a1, a2, a3]
                hg=60
                if self.queue_q[self.g+i][7]!="-":
                    a4 =QCheckBox(self)
                    a4.stateChanged.connect(self.onStateChanged)
                    sas.append(a4)
                    ot=10
                    hg=55
                for j in range(len(sas)):
                        sas[j].setText(self.queue_q[self.g+i][j+4])
                        sas[j].resize(510, 80)
                        sas[j].move(50, 550-ot-hg*j)
                        sas[j].hide()
                        word_wrap(sas[j])
                        masas.append(sas[j])
                
                
                self.big_queue.append(masas)
                
                
        #print(len(self.big_queue))
        
        for i in range(len(self.big_queue[self.g])):
            self.big_queue[self.g][i].show()
        button_sl = QPushButton("->", self)
        button_sl.setCheckable(True)
        button_sl.resize(60, 60)
        button_sl.clicked.connect(self.the_button_was_clicked)
        button_sl.move(620,500)
        button_sl.show()
        button_s2 = QPushButton("<-", self)
        button_s2.setCheckable(True)
        button_s2.resize(60, 60)
        button_s2.clicked.connect(self.the_button_was_clicked)
        button_s2.move(560,500)
        button_s2.show()
 
    def the_button_was_clicked(self):
            if len(self.ans_q)<=self.g:
                dlg = QDialog(self)
                dlg.setWindowTitle("ВЫБИРИТЕ ВАРИАНТ ОТВЕТА!")
                dlg.resize(400, 50)
                dlg.exec()
            else:
                for i in range(len(self.big_queue[self.g])):
                    self.big_queue[self.g][i].hide()
                #check if the right answer was chosen and put inf into table
                
                rec=[]
                if self.queue_q[self.g][8]==self.ans_q[self.g]:
                    
                    rec.append(True)
                else:
                    rec.append(False)
                
                rec.append(self.g+1)                
                rec.append(self.queue_q[self.g][1])
                rec.append(self.ans_q[self.g])
                rec.append(self.queue_q[self.g][8])                
                self.tabel.append(rec)
                self.g+=1
                self.reload()
    def reload(self):
        if self.g>=len(self.big_queue):
            for i in range(len(self.big_queue[self.g-1])):
                self.big_queue[self.g-1][i].hide()
            self.sender().hide()
            self.tabel_show()
        else:
            for i in range(len(self.big_queue[self.g])):
                self.big_queue[self.g][i].show()
    def onStateChanged(self):
        if self.sender().isChecked():
            if len(self.ans_q)>self.g:
                self.ans_q.pop(self.g)       
            self.ans_q.append(self.sender().text())

    def tabel_show(self):
        tb=QTableWidget(len(self.big_queue)+1, 4, self)
        tb.setHorizontalHeaderLabels(["Номер", "Категория", "Правильный ответ", "Ответ"])
        tb.setColumnWidth(1, 140)
        tb.setColumnWidth(2, 200)
        tb.setColumnWidth(3, 200)
        tb.setColumnWidth(0, 30)
        ct=0
        for i in range(self.g):
            for m in range(4):
                tb.setItem(i,m, QTableWidgetItem(str(self.tabel[i][m+1])))
                if m==3:
                    col=()
                    if self.tabel[i][0]:
                        col=(0, 255, 0)
                        ct+=1
                    else:
                        col=(255, 0, 0)
        s=QTableWidgetItem(str(ct))            
        tb.setItem(len(self.big_queue),0, QTableWidgetItem(str(ct)))    
        tb.resize(785, 600)
        tb.show()
        
    #def update(self):
        
        
        
        
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()


sys.exit(app.exec())
