import time
from dataURL import DataURL
from getURL import GetURL
from tkinter import *

useDataURL = DataURL()
useGetURL = GetURL()

pencere = Tk()
pencere.title("Pyhton Arayüz Ekleme")

canvas = Canvas(pencere, height=300, width=500)
canvas.pack()

etiket = Label(pencere, text="Mini Örümceğe Hoşgeldiniz", font=("Times New Roman", 15))
etiket.pack()

etiket1 = Label(pencere, text = "Hoşçakalın")
etiket.place(x=200, y=13)
etiket1.pack()


buton1= Button(pencere)
buton1.config(text="URL Listele", font=("Times New Roman", 10))
buton1.config(bg="black", fg="white")
buton1.place(x=200,y=60)

buton1= Button(pencere)
buton1.config(text="URL Ekle", font=("Times New Roman", 10))
buton1.config(bg="black", fg="white")
buton1.place(x=200,y=90)

buton2= Button(pencere)
buton2.config(text="Örümcek Gönder", font=("Times New Roman", 10))
buton2.config(bg="black", fg="white")
buton2.place(x=200, y=120)

buton3=Button(pencere)
buton3.config(text="Sonuçları Listele", font=("Times New Roman", 10))
buton3.config(bg="black", fg="white")
buton3.place(x=200, y=150)

buton4=Button(pencere)
buton4.config(text="Çıkış", font=("Times New Roman", 10))
buton4.config(bg="black", fg="white")
buton4.place(x=200, y=180)

pencere.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

print("-: Mini Örümceğe hoş geldiniz! :-")
print("|------------------------------|")
print("")
time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    print("Lütfen seçiminizi giriniz!")
    menuSecim = (input("Tercihiniz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
        elif menuSecim>=4:
            print("Menü numarası 0-4 arasında olmalıdır!")
    else:
        print("Menü numaranızı doğru yazdığınıza emin olun!")
