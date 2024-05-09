from pickle import FALSE
import sys
import headder
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import  QDialog, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QMessageBox, QButtonGroup, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy
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
    start_widget = [] #Интерфейс главного окна
    exam_widget = [] #Интерфейс экзаминационного окна
    big_queue=[]
    ans_q=[]
    tabel=[]
    g=0
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Экзамен по ПДД")
        self.resize(1024, 600)
        #self.setFixedSize(1024, 600)
        fff =  open('ui_ss.css', 'r')
        style = fff.read()
        self.setStyleSheet(style)
        self.start_widget.append(QWidget(self)) 
        
        layout = QVBoxLayout() #Главный шаблон окна

        button_st = QPushButton("Начать экзамен")
        button_st.setCheckable(True)
        #button_st.resize(150, 80)
        button_st.clicked.connect(self.exam)
        layout.addWidget(button_st)

        button_st1 = QPushButton("Посмотреть статистику")
        button_st1.setCheckable(True)
        #button_st1.resize(200, 80)
        
        # button_st1.clicked.connect(self.exam)
        layout.addWidget(button_st1)
        layout.setContentsMargins(200,20,200,20)
        self.start_widget[0].setLayout(layout)

        self.setCentralWidget(self.start_widget[0])

    def exam(self):
        self.sender().hide()
        self.start_widget[0].hide()
        self.exam_widget.append(QWidget(self)) 
        layout = QVBoxLayout() #Главный шаблон окна
        sas_layout = QVBoxLayout() #Тут всё понятно
        buttons_Vlayaut = QVBoxLayout()
        buttons_Hlayaut = QHBoxLayout()
        down_layout = QHBoxLayout()
        
        

        
        for i in range(len(self.queue_q)):
            masas = []           
            label = QLabel(self.queue_q[self.g+i][2], self)
            layout.addWidget(label)
            lb = QLabel(self)
            label.setWordWrap(True)
            label.resize(785, 100)
            if str(self.queue_q[self.g+i][3]) != '-':
                print(str(self.queue_q[self.g+i][3]))
                

                lb.move(65, 110)
                lb.resize(720, 480)
                lb.setPixmap(QPixmap(str(self.queue_q[self.g+i][3])).scaled(lb.size()))
                layout.addWidget(lb)
            label.hide()
            lb.hide()
            sas = []
            
            masas.append(label)
            masas.append(lb)
            #a1 = QCheckBox(self)
            #a2 = QCheckBox(self)
            #a3 = QCheckBox(self)
            ot = 50 #Отступы (Можно было назвать padding😡😡😡)
            #a1.stateChanged.connect(self.onStateChanged)
            #a2.stateChanged.connect(self.onStateChanged)
            #a3.stateChanged.connect(self.onStateChanged)
            sas.append(QCheckBox(self))
            sas.append(QCheckBox(self))
            sas.append(QCheckBox(self))
            hg = 60
            if self.queue_q[self.g+i][7] != "-":
                #a4 = QCheckBox(self)
                #a4.stateChanged.connect(self.onStateChanged)
                sas.append(QCheckBox(self))
                ot = 10
                hg = 55
            a = 0
            for checkbox in sas:
                checkbox.setText(self.queue_q[self.g+i][sas.index(checkbox) + 4])
                #checkbox.resize(510, 80)
                #checkbox.move(50, 550-ot-hg*a)
                checkbox.hide()
                checkbox.stateChanged.connect(lambda state, sas=sas: self.onStateChanged(sas))
                word_wrap(checkbox)
                masas.append(checkbox)
                a+=1
                sas_layout.addWidget(checkbox)
            self.big_queue.append(masas)

        for i in range(len(self.big_queue[self.g])):
            self.big_queue[self.g][i].show()
        
        button_sl = QPushButton("->️", self)
        button_sl.setCheckable(True)
        button_sl.resize(60, 60)
        button_sl.clicked.connect(self.the_button_was_clicked)
        button_sl.move(620,500)
        button_sl.setStyleSheet("font-size: 15pt;")
        button_sl.show()

        button_s2 = QPushButton("<-", self)
        button_s2.setCheckable(True)
        button_s2.resize(60, 60)
        button_s2.clicked.connect(self.the_button_was_clicked)
        #button_s2.move(560,500)
        button_s2.setStyleSheet("font-size: 15pt;")
        button_s2.show()
        buttons_Hlayaut.addSpacing(200)
        buttons_Hlayaut.addWidget(button_s2)
        buttons_Hlayaut.addWidget(button_sl)
        #buttons_Hlayaut.setContentsMargins(20,80,20,20)
            
        buttons_Vlayaut.addLayout(buttons_Hlayaut)

        down_layout.addLayout(sas_layout)
        down_layout.addLayout(buttons_Vlayaut)
        layout.addLayout(down_layout)
        self.exam_widget[0].setLayout(layout)
        self.setCentralWidget(self.exam_widget[0])

    def the_button_was_clicked(self):
            if len(self.ans_q)<=self.g:
                
                #dlg = QDialog(self)
                #dlg.setWindowTitle("ВЫБИРИТЕ ВАРИАНТ ОТВЕТА!")
                #dlg.resize(400, 50)
                #dlg.exec()
                
                #Здесь возможно больше подойдёт это окно:
                QMessageBox.information(self, "Экзамен по ПДД", "Пожалуйста, выберите вариант ответа!")

                
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
            self.sender().setChecked(False) 
    def reload(self):
        if self.g>=len(self.big_queue):
            for i in range(len(self.big_queue[self.g-1])):
                self.big_queue[self.g-1][i].hide()
            self.sender().hide()
            self.tabel_show()
        else:
            for i in range(len(self.big_queue[self.g])):
                self.big_queue[self.g][i].show()
    def onStateChanged(self, sas):
        if self.sender().isChecked():
            if len(self.ans_q)>self.g:
                self.ans_q.pop(self.g)
            for checkbox in sas:
                if self.sender() != checkbox:
                    if checkbox.isChecked():
                        checkbox.setChecked(False)
                
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
