import sqlite3 as sl

base = sl.connect('data.db')

with base:
    data = base.execute("select count(*) from sqlite_master where type='table' and name='questions'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
             base.execute("""
                 CREATE TABLE questions(
                 number INTEGER PRIMARY KEY,
                 cathigory VARCHAR(40),
                 text VARCHAR(500),
                 
                 image_adress VARCHAR(40),
                 aswer_one VARCHAR(200),
                 aswer_two VARCHAR(200),
                 aswer_three VARCHAR(200),
                 aswer_four VARCHAR(200),
                 right_answer VARCHAR(200)
               );
            """)

sql = 'INSERT or IGNORE INTO questions (number, cathigory, text, image_adress, aswer_one, aswer_two, aswer_three, aswer_four, right_answer) values(?, ?, ?, ?, ?, ?, ?, ?, ?)'
#data.execute("""DROP TABLE questions""")
def fill_bill():
    data=[]
    base = sl.connect('data.db')
    shesh= base.execute("SELECT number FROM questions")
    mas=[]
    for row in shesh:
        mas.append(row[0])
    if not len(mas)==0:
        top=max(mas)
    else:
        top=0
    k=top
    
    f=open('qsp.txt')
    for i in range(42):
        l=[]
        k+=1
        l.append(k)
        s=f.readline()
        for i in range(1, 9):
            a=f.readline()
            l.append(a[:-1:])
        m=(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
        #if s[:-1:]=='14':
            #print(m)
        data.append(m)
    with base:
        base.executemany(sql, data)   
    '''    
    text=str(input('Введите текст вопросса: '))
    cath = str(input('Введите категорию вопроса: '))
    path=str(input('Введите '))
    a1=str(input('Введите ответ 1: '))
    a2=str(input('Введите ответ 2: '))
    a3=str(input('Введите ответ 3: '))
    a4=str(input('Введите ответ 4: '))
    r_a=str(input('Введите правильный ответ: '))
        l=(k, cath,  text, path, a1, a2, a3, a4, r_a)'''
        
    
'''data = [
    (1, 'общие положения', 'В каком случае водитель совершит вынужденную остановку?', '-',  'Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу', 'Остановившись на проезжей части из-за технической неисправности транспортного средства', 'В обоих перечисленных случаях', '-',  'Остановившись на проезжей части из-за технической неисправности транспортного средства'),
    (2, 'общие положения', 'Сколько полос для движения имеет данная дорога?', '-',  'Две', 'Четыре', 'Пять', '-', 'Четыре')
    #(3, '')
]'''
def delete_last():
    data=[]
    base = sl.connect('data.db')
    shesh= base.execute("SELECT number FROM questions")
    mas=[]
    for row in shesh:
        mas.append(row[0])
    if not len(mas)==0:
        top=max(mas)
    else:
        top=0
    k=top
    shesh= base.execute("DELETE from questions WHERE number=?", (k, ))
a=[]
'''g=int(input())
if g==0:
    delete_last()'''
#fill_bill()
#g=int(input())
def check_cath():
    shesh= base.execute("SELECT cathigory FROM questions")
    mas=[]
    for row in shesh:
        mas.append(row[0])
    print(len(mas))
    cath=[]
    ind=[]
    for i in range(len(mas)):
        if not mas[i] in cath:
            cath.append(mas[i])
            ind.append(1)
        else:
            ind[cath.index(mas[i])]+=1
    for i in range(len(cath)):
        print(str(cath[i])+' = '+str(ind[i]))
        
    #print(mas)
#check_cath()
'''if g==0:
    delete_last()'''
with base:
    data = base.execute("SELECT cathigory FROM questions")
    for row in data:
        a.append(row)
        #print(row)

