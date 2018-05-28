from tkinter import *
from tkinter import messagebox
import requests, bs4 
import sys
import io
from contextlib import redirect_stdout

def pogoda(city): #функция с погодой на сегодняшний день
    city=city.get()
    s=requests.get('https://sinoptik.com.ru/погода-'+city) #URL сайта, откуда берется информация о городе и его погоде
    b=bs4.BeautifulSoup(s.text, "html.parser")

    buffer = io.StringIO()

    p = b.select('.rSide .description') #краткое описание
    pogoda = p[0].getText()
    print('\n '+pogoda.strip()+'\n', file=buffer)

    p3=b.select('.temperature .p3') #температура утром
    pogoda1=p3[0].getText()
    p4=b.select('.temperature .p4')
    pogoda2=p4[0].getText()
    p5=b.select('.temperature .p5') #тепература днём
    pogoda3=p5[0].getText()
    p6=b.select('.temperature .p6')
    pogoda4=p6[0].getText()  
    print(' Утром ' + pogoda1 + ' ' + pogoda2, file=buffer)
    print(' Днём ' + pogoda3 + ' ' + pogoda4, file=buffer)

    s=b.select('.infoDaylight') #восход и закат
    sun=s[0].getText()
    print(sun,file=buffer)

    v=b.select('.weatherDetails .p5') #давление
    davlenie=v[4].getText()  
    print(' Давление '+davlenie+' мм',file=buffer)

    vlazhnost=v[5].getText()  #влажность
    print(' Влажность '+vlazhnost+' %',file=buffer)

    veter=b.select('.gray .p5') #направление и скорость ветра
    veter2=veter[2].find("div")["data-tooltip"]
    print(' Ветер '+veter2,file=buffer)

    osadki=v[7].getText()  #вероятность осадков
    print(' Вероятность осадков '+osadki+' %',file=buffer)
    output = buffer.getvalue()
    return output


def pogoda2(city): #функция с погодой на неделю
    city=city.get()
    s=requests.get('https://sinoptik.com.ru/погода-'+city)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    buffer2 = io.StringIO()
    p = b.select('.tabs .main')
    i=0
    while i!=7:
        day = p[i].getText() #температура каждого дня
        print(day,file=buffer2)
        i=i+1
        number="bd"+str(i)
        desc2=b.find("div",attrs={"id":number}) #описание погоды каждого дня
        desc3=desc2.find("div",attrs={"class":"weatherIco"})["title"]
        print(" ",desc3,"\n",file=buffer2)
    output2 = buffer2.getvalue()
    return output2


top = Tk()
top.geometry("400x200")
top.title('Forecast')

def pogodaMsg():
    msg = messagebox.showinfo("Результат",pogoda(city))
def pogoda2Msg():
    msg = messagebox.showinfo("Результат",pogoda2(city))

   
L1 = Label(top, text = "Введите город")
L1.place(x = 50,y = 50)
city = Entry(top, bd = 5)
city.place(x = 200,y = 50)


B = Button(top, text = "Погода на сегодня", command = pogodaMsg)
B.place(x = 50,y = 100)

B = Button(top, text = "Погода на неделю", command = pogoda2Msg)
B.place(x = 200,y = 100)


top.mainloop()
