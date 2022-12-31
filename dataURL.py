
import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrolHTTP = siteURL[:7]  #http
    kontrolHTTPS = siteURL[:8]  #https
    http = "http://"
    https = "https://"
    if kontrolHTTP == http or kontrolHTTPS == https:
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        print("URL kaydedilmiştir.")
    else:
        print("Lütfen URL'nin ön ekini (/'https://' veya 'http://') şeklinde giriniz.")

  def dataRead(self):
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Henüz kaydedilmiş adres yoktur!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()