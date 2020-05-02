#!/usr/bin/env python
# coding: utf-8

# In[35]:


import docxtpl # работа с шаблоном печатной формы
from docxtpl import DocxTemplate
import datetime
import random
import csv # для кода 1 и 2 лабораторных работ
from docx2pdf import convert # код писался под macOS, однако на Windows должен тоже работать


# In[36]:


#Lab1
clientN = str(915783624)

def callTar(direction, dur):
    if direction == 'o':
        myVarOfTar = 2
    elif direction == 'i':
        myVarOfTar = 0
    else:
        print('I\'m gay')
    return float(myVarOfTar * dur)

def messTar(number):
    myNumOfTar = 10
    myTar = 1
    if number <= myNumOfTar:
        return 0
    return myTar * (number-myNumOfTar)

def biller1(a):
    bill = 0.0
    for row in csvReader:
        if row['msisdn_origin'] == a:
            bill += callTar('o',float(row['call_duration']))
            bill += messTar(int(row['sms_number']))
        elif row['msisdn_dest'] == a:
            bill += callTar('i', float(row['call_duration']))
    return bill


# In[37]:


#Lab2
clientI = "217.15.20.194"
myNumOfTar = pow(1024,2)

def intTar(number):
    myTar = 0.5
    res = (number / myNumOfTar)
    return  res * myTar

def biller2(a):
    bill = 0.0
    byteCount = 0
    dateRewrite1 = ''
    dateRewrite2 = ''
    for row in csvReader:
        if row['da'] == a: # ищем вхождения с нашим абонентом
            byteCount += (int(row['ibyt']))
    bill += intTar(byteCount) 
    return bill # рассчитываем сумму к оплате


# In[38]:


def generator(lenn):  # генератор для заполнения численных значений
    res = ''
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for i in range(lenn):
        a = random.choice(numbers)
        res += str(a)
    return res


# In[39]:


def dategen(mode):  # генератор для заполнения значений дат
    month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
    if mode == 'd':
        a = random.choice(day)
        return str(a)
    if mode == 'm':
        a = random.choice(month)
        return str(a)
    else:
        return 'three hundred bucks'


# In[40]:


def numToText(num1): # функция для создания прописного аналога значения счета
    num = num1
    cents = round(num - int(num), 2)
    num = int(num)
    th = ['Одна тысяча', 'Две тысячи', 'Три тысячи', 'Четыре тысячи', 'Пять тысяч', 'Шесть тысяч', 'Семь тысяч', 'Восемь тысяч', 'Девять тысяч']
    hun = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    Hun = ['Сто', 'Двести', 'Триста', 'Четыреста', 'Пятьсот', 'Шестьсот', 'Семьсот', 'Восемьсот', 'Девятьсот']
    dec = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    Dec = ['Двадцать', 'Тридцать', 'Сорок', 'Пятьдесят', 'Шестьдесят', 'Семьдесят', 'Восемьдесят', 'Девяносто']
    teen = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    Teen = ['Одиннадцать', 'Двенадцать', 'Тринадцать', 'Четырнадцать', 'Пятнадцать', 'Шестнадцать', 'Семнадцать', 'Восемнадцать', 'Девятнадцать']
    nums = ['один рубль', 'два рубля', 'три рубля', 'четыре рубля', 'пять рублей', 'шесть рублей', 'семь рублей', 'восемь рублей', 'девять рублей']
    Nums = ['Один рубль', 'Два рубля', 'Три рубля', 'Четыре рубля', 'Пять рублей', 'Шесть рублей', 'Семь рублей', 'Восемь рублей', 'Девять рублей']
    res = ''
    if num // 10000 > 0:
        print('Число слишком большое')
        return num
    if num // 1000 > 0:
        res += th[num//1000 - 1]
        res += ' '
        num = num % 1000
    if num // 100 > 0:
        if res == '':
            res += Hun[num//100 - 1]
            res += ' '
            num = num % 100
        else:
            res += hun[num//100 - 1]
            res += ' '
            num = num % 100
    if num // 10 >= 2:
        if res == '':
            res += Dec[num//10 - 2]
            res += ' '
            num = num % 10
        else:
            res += dec[num//10 - 2]
            res += ' '
            num = num % 10
    if num // 10 == 1:
        if res == '':
            res += Teen[num%10 - 1]
            res += ' '
        else:
            res += teen[num%10 - 1]
            res += ' '
    if num % 10 > 0 and num // 10 !=1:
        if res == '':
            res += Nums[num%10 - 1]
            res += ' '
        else:
            res += nums[num%10 - 1]
            res += ' '
    res += str(int(cents*100))
    if int(cents*100) % 10 == 1:
        res += ' копейка'
    elif int(cents*100) % 10 == 2 or int(cents*100) % 10 == 3 or int(cents*100) % 10 == 4:
        res += ' копейки'
    else:
        res += ' копеек'
    return res


# In[41]:


inp = "/Users/romanbelov/Documents/Lab3inp.docx"
outp = "/Users/romanbelov/Documents/Lab3Outp.docx"
#Lab1
with open('/Users/romanbelov/Downloads/lab1.csv', 'r', newline='') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter=',')
    billM = biller1(clientN)
    csvfile.close()
#Lab2
with open('/Users/romanbelov/Documents/lab2inp2.csv', 'r', newline='') as csvfile: 
    csvReader = csv.DictReader(csvfile, delimiter=',')
    billI = round(biller2(clientI), 2)
    csvfile.close()
#Lab3
# заполняем переменные
now = datetime.datetime.now()
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
day = str(now.day)
month = months[now.month - 1]
year34 = str(now.year)[2:]
billNum = generator(2)
cliInn = generator(12)
cliKpp = generator(9)
cliIndex = generator(6)
cliAddr = 'г. Москва, ул. Свободы, д. 15'
cliName = 'ООО \"Невероятные приключения ДжоДжо\"'
idNum = generator(8)
osnDate = dategen('d') +' '+ dategen('m') +' '+ str(now.year)
#billM = 77.46
#billI = 84.24
total = billM + billI
tax = round(0.2 * total, 2)
textstr = numToText(total)


# In[43]:


doc = DocxTemplate(inp)  # заполняем шаблон нужными значениями
context = { 'bankName' : 'АО \"TikTok это круто\", Г. САНКТ-ПЕТЕРБУРГ', 'bicB' : '133737133', 'accN' : '13371337133713371337',
           'inn1' : '133713371337', 'kpp1' : '133713371', 'billN' : '1111101111000011',
           'ourName' : 'ООО \"Привет, Андрей\"', 'num' : billNum, 'day' : day, 'month' : month,
           'year34' : year34, 'index1' : '191111', 'address1' : 'г. Санкт-Петербург, ул. Ломоносова, д. 9',
           'clientName' : cliName, 'inn2' : cliInn, 'kpp2' : cliKpp, 'index2' : cliIndex, 'address2' : cliAddr,
           'id' : idNum, 'osnDate' : osnDate, 'service1' : 'Мобильная связь', 'service2' : 'Интернет', 
           'bill1' : str(billM), 'bill2' : str(billI), 'fistingIs' : str(total), 'tax' : str(tax),'textsum' : textstr,
           'dungeonMaster' : 'Белов Р.Д.', 'bugh' : 'Папушкина Е.М.',
          }
doc.render(context)
doc.save(outp)
convert(outp, "/Users/romanbelov/Documents/Lab3Outp.pdf")


# In[ ]:




