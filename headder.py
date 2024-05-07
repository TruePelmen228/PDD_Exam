import sqlite3 as sl
import random
#import mysql.connector

NAME_OF_DB_Q='data.db'
NAME_OF_DB_A=''

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
    print(hm)
    if len(mas)!=0:
        k= not x in mas
    else:
        k=1
    num_set=[]
    
    while len(num_set)<5:
        x=random.randrange(min(hm), max(hm)+1)
        if (not x in num_set) and (x in hm) and k:
            num_set.append(x)
    print(num_set) 
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
take_five('скорость движения', h)

class answer(base ):

    def __init__(self, num_ses, number, ans, right_answer):
        self.num_ses = num_ses
        self.number = number
        self.ans = ans
        self.right_answer = right_answer

    #def reFill_it():
        #function wich takes fields of obj into "answers" table
