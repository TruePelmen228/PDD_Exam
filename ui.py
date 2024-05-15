from pickle import FALSE
import sys
import headder
from PyQt6.QtGui import QPixmap, QFont, QColor
from PyQt6.QtWidgets import  QDialog, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QMessageBox, QButtonGroup, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt6.QtCore import QTimer
import datetime





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
    queue_q=headder.take_five('скорость движения', h)+headder.take_five('остановка и стоянка', h)+headder.take_five('дорожные знаки', h)+headder.take_five('общие положения', h)
    start_widget = [] #Интерфейс главного окна
    exam_widget = [] #Интерфейс экзаминационного окна
    current_issue = 0
    big_queue=[]
    ans_q=[]
    tabel=[]
    ans_rec=[]
    timer = QTimer()
    
    exam_time = 0
    timer_str = ""
    timer_labels = []
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
        
        button_st1.clicked.connect(self.statistics)
        layout.addWidget(button_st1)
        layout.setContentsMargins(200,20,200,20)
        self.start_widget[0].setLayout(layout)

        self.setCentralWidget(self.start_widget[0])

    def exam(self):
        now = datetime.datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        print(self.current_time)
        #print(current_time)
        #self.sender().hide()
        self.exam_time = 1200
        self.sender().setChecked(False) 
        self.start_widget[0].hide()
        self.start_widget[0] = self.takeCentralWidget()
        self.timer.timeout.connect(self.processOneThing)
        


        
        for i in range(len(self.queue_q)):
            q_widget =  QWidget(self)
            self.exam_widget.append(q_widget) 
        
            layout = QVBoxLayout() #Главный шаблон окна
            sas_layout = QVBoxLayout() #Тут всё понятно
            buttons_Vlayaut = QVBoxLayout()
            buttons_Hlayaut = QHBoxLayout()
            down_layout = QHBoxLayout()
            
            masas = []           
            label = QLabel(self.queue_q[self.current_issue+i][2], self)
            self.timer_labels.append(QLabel(self))
            buttonlabel_Hlayaut = QHBoxLayout()
            
            button_stop = QPushButton("X", self)
            button_stop.setCheckable(True)
            button_stop.clicked.connect(self.the_button_stop_was_clicked)
            button_stop.setStyleSheet("font-size: 16pt;")
            button_stop.setFixedSize(60,60)
            button_stop.show()

            buttonlabel_Hlayaut.addWidget(button_stop)
            buttonlabel_Hlayaut.addWidget(label)
            
            layout.addLayout(buttonlabel_Hlayaut)
            layout.addWidget(self.timer_labels[i])
            layout.addSpacerItem(QSpacerItem(10,10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
            lb = QLabel(self)
            label.setWordWrap(True)
            label.resize(785, 100)
            if str(self.queue_q[self.current_issue+i][3]) != '-':
                print(str(self.queue_q[self.current_issue+i][3]))
                

                #lb.move(65, 110)
                lb.resize(750, 280)
                lb.setPixmap(QPixmap(str(self.queue_q[self.current_issue+i][3])).scaled(lb.size()))
                layout.addWidget(lb)
                layout.insertSpacing(4,150)
            else:
                layout.insertSpacing(2,400)
            #label.hide()
            #lb.hide()
            sas = []
            
            masas.append(label)
            masas.append(lb)
            #a1 = QCheckBox(self)
            #a2 = QCheckBox(self)
            #a3 = QCheckBox(self)
            #ot = 50 #Отступы (Можно было назвать padding😡😡😡)
            #a1.stateChanged.connect(self.onStateChanged)
            #a2.stateChanged.connect(self.onStateChanged)
            #a3.stateChanged.connect(self.onStateChanged)
            sas.append(QCheckBox(self))
            sas.append(QCheckBox(self))
            sas.append(QCheckBox(self))
            hg = 60
            if self.queue_q[self.current_issue+i][7] != "-":
                #a4 = QCheckBox(self)
                #a4.stateChanged.connect(self.onStateChanged)
                sas.append(QCheckBox(self))
                ot = 10
                hg = 55
            a = 0
            for checkbox in sas:
                checkbox.setText(self.queue_q[self.current_issue+i][sas.index(checkbox) + 4])
                #checkbox.resize(510, 80)
                #checkbox.move(50, 550-ot-hg*a)
                #checkbox.hide()
                checkbox.stateChanged.connect(lambda state, sas=sas: self.onStateChanged(sas))
                word_wrap(checkbox)
                masas.append(checkbox)
                a+=1
                sas_layout.addWidget(checkbox)
            self.big_queue.append(masas)
            
            button_sl = QPushButton("->", self)
            button_sl.setCheckable(True)
            button_sl.resize(60, 60)
            button_sl.clicked.connect(lambda state, sas=sas: self.the_button_was_clicked(sas))
            button_sl.move(620,500)
            button_sl.setStyleSheet("font-size: 15pt;")
            button_sl.setFixedSize(60,60)
            button_sl.show()

            button_s2 = QPushButton("<-", self)
            button_s2.setCheckable(True)
            button_s2.resize(60, 60)
            button_s2.clicked.connect(self.the_button_back_was_clicked)
            #button_s2.move(560,500)
            button_s2.setStyleSheet("font-size: 15pt;")
            button_s2.setFixedSize(60,60)
            button_s2.show()
            buttons_Hlayaut.addSpacing(200)
            buttons_Hlayaut.addWidget(button_s2)
            buttons_Hlayaut.addWidget(button_sl)
            #buttons_Hlayaut.setContentsMargins(20,80,20,20)
            
            buttons_Vlayaut.addLayout(buttons_Hlayaut)

            down_layout.addLayout(sas_layout)
            down_layout.addLayout(buttons_Vlayaut)
            layout.addLayout(down_layout)
            self.exam_widget[i].setLayout(layout)
            self.exam_widget[i].hide()
            

        for i in range(len(self.big_queue[self.current_issue])):
            self.big_queue[self.current_issue][i].show()
        self.exam_widget[self.current_issue].show()
        self.setCentralWidget(self.exam_widget[self.current_issue])
        self.timer.start(1000)
        self.set_time_srt()
        
        
        

    def the_button_was_clicked(self, sas):
            #if len(self.ans_q)<=self.current_issue:
            is_checked = False
            for checkbox in sas:
                if checkbox.isChecked():
                    is_checked = True
                    break
            if not(is_checked):

                    QMessageBox.information(self, "Экзамен по ПДД", "Пожалуйста, выберите вариант ответа!")
                    #dlg = QDialog(self)
                    #dlg.setWindowTitle("ВЫБИРИТЕ ВАРИАНТ ОТВЕТА!")
                    #dlg.resize(400, 50)
                    #dlg.exec()
                
               

                
            else:
                # for i in range(len(self.big_queue[self.current_issue])):
                #     self.big_queue[self.current_issue][i].hide()
                self.exam_widget[self.current_issue].hide()
                
                #check if the right answer was chosen and put inf into table
                
                rec=[]
                if self.queue_q[self.current_issue][8]==self.ans_q[self.current_issue]:
                    
                    rec.append(True)
                else:
                    rec.append(False)
                
                rec.append(self.current_issue+1)                
                rec.append(self.queue_q[self.current_issue][1])
                rec.append(self.ans_q[self.current_issue])
                rec.append(self.queue_q[self.current_issue][8])                
                self.tabel.append(rec)
                self.current_issue+=1
                self.out_of_bt()
                
            self.set_time_srt()
            self.sender().setChecked(False) 
    
    def the_button_stop_was_clicked(self):
        reply = QMessageBox.question(self, 'Экзамен по ПДД', 'Вы уверены, что хотите прервать экзамен?', QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        self.sender().setChecked(False) 
        if reply == QMessageBox.StandardButton.Yes:
            self.exam_widget.clear()
            self.current_issue = 0
            self.big_queue.clear()
            self.ans_q.clear()
            self.tabel.clear()
            self.timer.stop()
            self.timer_labels.clear()
            self.setCentralWidget(self.start_widget[0])
            self.start_widget[0].show()
            

        
    def the_button_back_was_clicked(self):
        if self.current_issue > 0:
                self.exam_widget[self.current_issue].hide()
                self.exam_widget[self.current_issue] = self.takeCentralWidget()
                self.current_issue = self.current_issue - 1
              
              
                self.setCentralWidget(self.exam_widget[self.current_issue])
                self.exam_widget[self.current_issue].show()
        self.sender().setChecked(False) 
        self.set_time_srt()

    def out_of_bt(self):
        if self.current_issue>=len(self.big_queue):
            for i in range(len(self.big_queue[self.current_issue-1])):
                self.big_queue[self.current_issue-1][i].hide()
            self.sender().hide()
            now = datetime.datetime.now()
            self.current_time1 = now.strftime("%H:%M:%S")
            print(self.current_time1)
            minuts =int(self.current_time1[3:5:])-int(self.current_time[3:5:])
            seconds =int(self.current_time1[6:8:])-int(self.current_time[6:8:])
            if seconds<0:
                minuts-=1
                seconds+=60
            self.ans_rec.append(minuts)
            self.ans_rec.append(seconds)
            self.tabel_show()
            self.timer.stop()
        else:
            # for i in range(len(self.big_queue[self.current_issue])):
            #     self.big_queue[self.current_issue][i].show()
            if self.current_issue >0:
                  self.exam_widget[self.current_issue-1] = self.takeCentralWidget()
            self.setCentralWidget(self.exam_widget[self.current_issue])
            self.exam_widget[self.current_issue].show()
            
            #self.exam()    
    #def reload(self):
        
    def processOneThing(self):
        self.exam_time = self.exam_time - 1
        self.set_time_srt()       

    def set_time_srt(self):
            
            minutes =    int(self.exam_time/int(60))
            seconds = self.exam_time  - minutes * 60
            sec = ""
            mins = ""
            if seconds < 10:
                sec = f"0{seconds}"
            else:
                sec = f"{seconds}"
            if minutes < 10:
                mins = f"0{minutes}"
            else:
                mins = f"{minutes}"
            self.timer_str = f"{mins}:{sec}"
            if len(self.queue_q) > self.current_issue:
                self.timer_labels[self.current_issue].setText(self.timer_str)
            
            

    def onStateChanged(self, sas):
        if self.sender().isChecked():
            if len(self.ans_q)>self.current_issue:
                self.ans_q.pop(self.current_issue)
            for checkbox in sas:
                if self.sender() != checkbox:
                    if checkbox.isChecked():
                        checkbox.setChecked(False)
                
            self.ans_q.append(self.sender().text())
            
    

    def tabel_show(self):
        tb=QTableWidget(len(self.big_queue), 4, self)
        tb.setHorizontalHeaderLabels(["Номер", "Категория", "Правильный ответ", "Ответ"])
        tb.setColumnWidth(1, 200)
        tb.setColumnWidth(2, 200)
        tb.setColumnWidth(3, 200)
        tb.setColumnWidth(0, 50)
        '''ct=0
        for i in range(self.current_issue):
            for m in range(4):
                tb.setItem(i,m, QTableWidgetItem(str(self.tabel[i][m+1])))
                if m==3:
                    col=()
                    if self.tabel[i][0]:
                        col=(0, 255, 0)
                        ct+=1
                    else:
                        col=(255, 0, 0)'''

        correct_color = QColor(130, 235, 158)
        incorrect_color = QColor(235, 130, 130)
        ct=0

        for i in range(self.current_issue):
            for m in range(4):
                item = QTableWidgetItem(str(self.tabel[i][m+1]))
                if m == 3:  
                    if self.tabel[i][0]:
                        item.setBackground(correct_color)
                        ct+=1
                    else:
                        item.setBackground(incorrect_color)
                tb.setItem(i, m, item)
        #self.ans_rec.append(self.current_time)
        #self.ans_rec.append(self.current_time1)
        self.ans_rec.append(ct)

        correct_count_label = QLabel(str(ct))
        #s=QTableWidgetItem(str(ct))            
        #tb.setItem(len(self.big_queue),0, QTableWidgetItem(str(ct)))    
        tb.resize(785, 600)
        #tb.sizePolicy = QSizePolicy.Policy.Maximum
        tb.show()
        correct_count_label.move(0, 650)
        correct_count_label.show()
        print(self.ans_rec)
        headder.put_ans(self.ans_rec)
        #correct_count_item = QTableWidgetItem(str(ct))
        #tb.setItem(len(self.big_queue), 0, correct_count_item)

    def statistics(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Статистика за последнее время")
        dlg.resize(500, 500)
        mas=headder.get_ans()
        tb=QTableWidget(len(mas), 3, dlg)
        tb.setHorizontalHeaderLabels(["Номер", "Время прохождения", "Кол-во правильных ответов"])
        tb.setColumnWidth(1, 200)
        tb.setColumnWidth(2, 200)
        tb.setColumnWidth(0, 50)
        for i in range(len(mas)):
            for m in range(3):
                if m==1:
                    secs=str(mas[i][2])
                    if len(secs)==1:
                        secs='0'+secs
                    mins=str(mas[i][1])
                    if len(mins)==1:
                        mins='0'+mins
                    time=mins+':'+secs
                    item = QTableWidgetItem(time)
                else:
                    item = QTableWidgetItem(str(mas[i][m]))
                tb.setItem(i, m, item)
        tb.show()
        dlg.exec()
        


    #def update(self):
        
        
        
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()


sys.exit(app.exec())
