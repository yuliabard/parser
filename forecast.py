import requests, bs4
import sys

def pogoda(city):
    s=requests.get('https://sinoptik.com.ru/погода-'+city)
    b=bs4.BeautifulSoup(s.text, "html.parser")

    p = b.select('.rSide .description') #описание
    pogoda = p[0].getText()
    print('\n '+pogoda.strip()+'\n')

    p3=b.select('.temperature .p3') #температура
    pogoda1=p3[0].getText()
    p4=b.select('.temperature .p4')
    pogoda2=p4[0].getText()
    p5=b.select('.temperature .p5')
    pogoda3=p5[0].getText()
    p6=b.select('.temperature .p6')
    pogoda4=p6[0].getText()  
    print(' Утром ' + pogoda1 + ' ' + pogoda2)
    print(' Днём ' + pogoda3 + ' ' + pogoda4)

    s=b.select('.infoDaylight') #восход и закат
    sun=s[0].getText()
    print(sun)

    v=b.select('.weatherDetails .p5') # давление
    davlenie=v[4].getText()  
    print(' Давление '+davlenie+' мм')

    vlazhnost=v[5].getText()  #влажность
    print(' Влажность '+vlazhnost+' %')

    veter=b.select('.gray .p5')
    veter2=veter[2].find("div")["data-tooltip"]
    print(' Ветер '+veter2)

    osadki=v[7].getText()  #вероятсность осадков
    print(' Вероятность осадков '+osadki+' %')
    return 0

def pogoda2(city):
    s=requests.get('https://sinoptik.com.ru/погода-'+city)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p = b.select('.tabs .main')
    i=0
    while i!=7:
        day = p[i].getText()
        print(day)
        i=i+1
        number="bd"+str(i)
        desc2=b.find("div",attrs={"id":number})
        desc3=desc2.find("div",attrs={"class":"weatherIco"})["title"]
        print(" ",desc3,"\n")

    
def main():
    city=input('Введите город:')
    x=1
    while x!=0:
        x=int(input('\n[1] Погода на сегодня\n[2] Погода на неделю\n[3] Другой город\n[0] Выход\n\n'))
        if x==1:
            pogoda(city)
        elif x==2:
            pogoda2(city)
        elif x==3:
            city=input('Введите город:')
    else:
        sys.exit()

if __name__ == '__main__':
    main()
