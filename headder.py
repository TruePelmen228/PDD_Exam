import sqlite3 as sl
import random
#import mysql.connector

NAME_OF_DB='data.db'


class base(object):
    def __init__(self, number, right_answer):
        self.number= number
        self.right_answer = right_answer

    def get_number(self):
        return self.number
        

        
class question(base):
    
    def __init__(self, number, cathigory, text, image_adress, aswer_one, aswer_two, aswer_three, aswer_four, right_answer):
        self.number= number
        self.cathigory = cathigory
        self.text = text
        self.image_adress =image_adress
        self.aswer_one = aswer_one
        self.aswer_two = aswer_two
        self.aswer_three = aswer_three
        self.aswer_four = aswer_four
        self.right_answer = right_answer

    def get_mas_of(self):
        mas=[]
        mas.append(self.number)
        mas.append(self.cathigory)
        mas.append(self.text)
        mas.append(self.image_adress)
        mas.append(self.aswer_one)
        mas.append(self.aswer_two)
        mas.append(self.aswer_three)
        mas.append(self.aswer_four)
        mas.append(self.right_answer)
        return mas
    

def take_five(x, mas):
    #take question with "x" cathigory
    base = sl.connect('data.db')
    take= base.execute("SELECT number FROM questions WHERE cathigory = ?;", (x, ))
    hm=[]
    
    for row in take:
        hm.append(row[0])
    #choose some random numbers of them
    #print(hm)
    k=0
    if len(mas)!=0:
        k= not x in mas
    else:
        k=1
    num_set=[]
    
    while len(num_set)<5:
        x=random.randrange(min(hm), max(hm)+1)
        if (not x in num_set) and (x in hm) and k:
            num_set.append(x)
    #print(num_set) 
    #make five questions with this numbers
    
    cath_mas=[]
    for i in num_set:
        cath_mas.append(fill_it(i))
    
    return cath_mas
def fill_it(x):   
    base = sl.connect('data.db')
    mas=[]        
    with base:
        data = base.execute("SELECT * FROM questions WHERE number = ?;", (x, ))
    
        for row in data:
            
        
        
            number=row[0]
        
            cathigory=row[1]
            text=row[2]
            image_adress=row[3]
            aswer_one=row[4]
            aswer_two=row[5]
            aswer_three=row[6]
            aswer_four=row[7]
            right_answer=row[8]
            n_q = question(number, cathigory, text, image_adress, aswer_one, aswer_two, aswer_three, aswer_four, right_answer)
            #print(row)
            mas=n_q.get_mas_of()

    return mas
h=[]
#take_five('скорость движения', h)
def standard_ex(h):
    base = sl.connect('data.db')
    take= base.execute("SELECT cathigory FROM questions")
    hm=[]
    for row in take:
        hm.append(row[0])
    s1=[]
    for i in range(len(hm)):
        if not hm[i] in s1:
            s1.append(hm[i])
  
    d=[]
    print(s1)
    mas=[]
    while len(mas)<20:
        s=random.randrange(0, len(s1))
        if not s in d:
            d.append(s)
            mas+=take_five(s1[s], h)
    return mas
print(standard_ex(h)[0])

class answer(base ):

    def __init__(self, num_ses, number, ans, right_answer):
        self.num_ses = num_ses
        self.number = number
        self.ans = ans
        self.right_answer = right_answer

    #def reFill_it():
        #function wich takes fields of obj into "answers" table


def put_ans(que_ans):
    base = sl.connect(NAME_OF_DB)
    data = base.execute("SELECT session_number FROM answers")
    cursor=base.cursor()
    sql = "INSERT INTO answers (time_m, time_s, mode, right_answers, of_w) values(?, ?, ?, ?, ?)"
    hm=[]    
    for row in data:
        hm.append(row[0])
    print(hm)
    if len(hm)==0:
        k=1
    else:
        k=max(hm)+1
    time_m = que_ans[0]
    time_s = que_ans[1]
    mode=que_ans[2]
    right_ans=que_ans[3]
    of_w=que_ans[4]
    #test=(1, 15, 20, 10)
    m=(time_m, time_s, mode, right_ans, of_w)
    
    print(m)
    #base.executemany(sql, sss)
    try:
        cursor.execute(sql, m)
        base.commit()
        print("status:", cursor.rowcount)

    except sqlite3.Error as e:
        print("ex:", e)
    base.close()
s=[13, 8, 10]
def get_ans():
    ans_mas=[]
    base = sl.connect(NAME_OF_DB)
    data = base.execute("SELECT session_number FROM answers")
    hm=[]    
    for row in data:
        hm.append(row[0])
    if max(hm)>15:
        hm=hm[-15::]
    for i in range(len(hm)):
        data1 = base.execute("SELECT * FROM answers WHERE session_number = ?;", (hm[i], ))
        rec=[]
        for row in data1:
            for j in range(6):
                rec.append(row[j])
        ans_mas.append(rec)
    print(ans_mas)
    return ans_mas
#get_ans()
