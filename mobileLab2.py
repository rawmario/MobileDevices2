#!/usr/bin/env python
# coding: utf-8

# In[5]:


# импортируем библиотекит для работы с csv, массивами и графиками
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# задаем параметры отображения графика
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')  
plt.rcParams['figure.figsize'] = (25, 5)  


# In[6]:


# интернет-тарификация 
def intTar(number):
    myTar = 0.5
    res = (number / myNumOfTar)
    return  res * myTar


# In[7]:


def biller(a):
    bill = 0.0
    byteCount = 0
    dateRewrite1 = ''
    dateRewrite2 = ''
    for row in csvReader:
        if row['da'] == a: # ищем вхождения с нашим абонентом, записываем объем трафика, заполняем массивы для графика
            byteCount += (int(row['ibyt']))
            dateRewrite1 = str(row['ts'])
            dateRewrite2 = dateRewrite1[0:16] # записываем значения до минут (поэтому берем первые 16 символов), поменяйте значение среза для последующей группировки по другим еденицам времени
            if x != []:
                counter = 0
                for i in x: 
                    if i == dateRewrite2:
                        y[counter] += float(int(row['ibyt'])/ myNumOfTar)
                        break
                    elif counter != len(x)-1:
                        counter +=1
                        continue
                    else:
                        x.append(dateRewrite2)
                        y.append(float(int(row['ibyt'])/ myNumOfTar))
                        break
            else:
                x.append(dateRewrite2)
                y.append(float(int(row['ibyt'])/ myNumOfTar))
    bill += intTar(byteCount) 
    return bill # рассчитываем сумму к оплате


# In[8]:


client = "217.15.20.194" # абонент, для которого рассчитываем тарификацию
myNumOfTar = pow(1024,2) # еденица расчета тарификации (МБ в моем варианте)

# поменяйте путь к csv-файлу для корректной работы 
with open('/Users/romanbelov/Documents/lab2inp2.csv', 'r', newline='') as csvfile: 
    csvReader = csv.DictReader(csvfile, delimiter=',')
    x = []
    y = []
# рассчитываем плату за период в таблице
    print('Для абонента', client,'плата составит', round(biller(client),2),'руб.')
# строим график, по оси x значения сгруппированны по минутам
    arr = np.array((x,y))
    sortedDates = np.sort(arr[0])
    arr[0] = sortedDates
    plt.bar(arr[0],arr[1].astype(float))
    plt.title('Распределение трафика пользователя за отчетный период')
    plt.xlabel('Дата и время')
    plt.ylabel('Количество мегабайт')
    plt.show()
    csvfile.close()

