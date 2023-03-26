
from tkinter import *
pencere = Tk()
pencere.title("Kullanici Girisi")
pencere.geometry("350x200")



s_kullanici_adi = "admin"
s_sifre = "12345"

def basarili_giris():
  mesaj = Label(text="Bilgiler Dogru\nSisteme basarili giris yaptiniz",fg="green")
  mesaj.pack()
  
def basarisiz_giris():
  mesaj = Label(text="Girilen Bilgiler Yalnis !/n Bilgileri Kontrol Edip Tekrar Deneyin", fg="red")
  mesaj.pack()

def kontrol():
  girilen_ad = str(ad.get())
  girilen_sifre = str(sifre.get())
  if girilen_ad == s_kullanici_adi and girilen_sifre:
    kul_adi.destroy()
    kul_sifre.destroy()
    ad.destroy()
    sifre.destroy()
    dugme.destroy()
    basarili_giris()
  else:
    basarisiz_giris()
    kul_adi.destroy()
    kul_sifre.destroy()
    ad.destroy()
    sifre.destroy()
    dugme.destroy()
    basarili_giris()

def giris():
  global ad,sifre,kul_adi,kul_sifre,dugme
  kul_adi = Label(text="Kullanici Adi")
  kul_adi.grid(row=0,column=0)
  kul_sifre = Label(text="Sifre")
  kul_sifre.grid(row=1,column=0)
  ad = Entry()
  ad.grid(row=0,column=1)
  sifre = Entry()
  sifre.grid(row=1,column=1)
  dugme = Button(text="Giris", width=15,command=kontrol)
  dugme.grid(row=2,column=1)
  
giris()

mainloop()
