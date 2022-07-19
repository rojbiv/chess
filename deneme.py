print("Hello World")

isim = input('isminizi giriniz : ')
print("merhaba "+isim)

kullanici_adim="python"

parolam ="1234"

giris_hakki=3

while giris_hakki>0:
       
     kullanici_adi = input("kullanıcı adınızı girin :")
     
     parola = input("parolanızı girin :")
     
     if kullanici_adi==kullanici_adim and parola==parolam:
     
         print ("yönlendiriliyorsunuz...")
         print("welcome to the "+kullanici_adim+" account :")
         break
         
     else:
         print("kullanıcı bilgilerinizi yanlış girdiniz.lütfen tekrar deneyiniz.kullanıcı bilgileriniz yoksa lütfen hesap açınız. ") 

yas = input('yasınız : ')
if(int(yas)<18):
       print("yasınız ehliyet için uygun değildir")
else:
       print("yasınız ehliyet almak için uygundur.")
        
memleket ="mardin"
köy ="başyurt"

giris_hakki=3

while giris_hakki>0:
     
     memleket = str(input("lütfen memleketinizi giriniz : "))
     
     köy = str(input("lütfen köyünüzü giriniz : "))
     
     if memleket=="mardin" and köy=="başyurt":
         print("doğru girdiniz.devam edebilirsiniz...")
         break 
         
     else:
         print("yanlış girdiniz.lütfen tekrar deneyin...")

plaka=input('plaka giriniz: ')

cikti = ""
if plaka == '01':
   print("Adana")
elif plaka == '02':
   print("ADIYAMAN")
elif plaka == '03':
   print("AFYONKARAHİSAR")
elif plaka == '04':
   print("AĞRI")
elif plaka == '05':
   print("AMASYA")
elif plaka == '06':
   print("ANKARA")
elif plaka == '07':
   print("ANTALYA")
elif plaka == '08':
   print("ARTVİN")
elif plaka == '09':
   print("AYDIN")
elif plaka == '10':
   print("BALIKESİR")
elif plaka == '11':
   print("BİLECİK")
elif plaka == '12':
   print("BİNGÖL")
elif plaka == '13':
   print("BİTLİS")
elif plaka == '14':
   print("BOLU")
elif plaka == '15':
   print("BURDUR")
elif plaka == '16':
   print("BURSA")
elif plaka == '17':
   print("ÇANAKKALE")
elif plaka == '18':
   print("ÇANKIRI")
elif plaka == '19':
   print("ÇORUM")
elif plaka == '20':
   print("DENİZLİ")
elif plaka == '21':
   print("DİYARBAKIR")
elif plaka == '22':
   print("EDİRNE")
elif plaka == '23':
   print("ELAZIĞ")
elif plaka == '24':
   print("ERZİNCAN")
elif plaka == '25':
   print("ERZURUM")
elif plaka == '26':
   print("ESKİŞEHİR")
elif plaka == '27':
   print("GAZİANTEP")
elif plaka == '28':
   print("GİRESUN")
elif plaka == '29':
   print("GÜMÜŞHANE")
elif plaka == '30':
   print("HAKKARİ")
elif plaka == '31':
   print("HATAY")
elif plaka == '32':
   print("ISPARTA")
elif plaka == '33':
   print("MERSİN")
elif plaka == '34':
   print("İSTANBUL")
elif plaka == '35':
   print("İZMİR")
elif plaka == '36':
   print("KARS")
elif plaka == '37':
   print("KASTAMONU")
elif plaka == '38':
   print("KAYSERİ")
elif plaka == '39':
   print("KIRKLARELİ")
elif plaka == '40':
   print("KIRŞEHİR")
elif plaka == '41':
   print("KOCAELİ")
elif plaka == '42':
   print("KONYA")
elif plaka == '43':
   print("KÜTAHYA")
elif plaka == '44':
   print("MALATYA")
elif plaka == '45':
   print("MANİSA")
elif plaka == '46':
   print("KAHRAMANMARAŞ")
elif plaka == '47':
   print("MARDİN")
elif plaka == '48':
   print("MUĞLA")
elif plaka == '49':
   print("MUŞ")
elif plaka == '50':
   print("NEVŞEHİR")
elif plaka == '51':
   print("NİĞDE")
elif plaka == '52':
   print("ORDU")
elif plaka == '53':
   print("RİZE")
elif plaka == '54':
   print("SAKARYA")
elif plaka == '55':
   print("SAMSUN")
elif plaka == '56':
   print("SİİRT")
elif plaka == '57':
   print("SİNOP")
elif plaka == '58':
   print("SİVAS")
elif plaka == '59':
   print("TEKİRDAĞ")
elif plaka == '60':
   print("TOKAT")
elif plaka == '61':
   print("TRABZON")
elif plaka == '62':
   print("TUNCELİ")
elif plaka == '63':
   print("ŞANLIURFA")
elif plaka == '64':
   print("UŞAK")
elif plaka == '65':
   print("VAN")
elif plaka == '66':
   print("YOZGAT")
elif plaka == '67':
   print("ZONGULDAK")
elif plaka == '68':
   print("AKSARAY")
elif plaka == '69':
   print("BAYBURT")
elif plaka == '70':
   print("KARAMAN")
elif plaka == '71':
   print("KIRIKKALE")
elif plaka == '72':
   print("BATMAN")
elif plaka == '73':
   print("ŞIRNAK")
elif plaka == '74':
   print("BARTIN")
elif plaka == '75':
   print("ARDAHAN")
elif plaka == '76':
   print("IĞDIR")
elif plaka == '77':
   print("YALOVA")
elif plaka == '78':
   print("KARABÜK")
elif plaka == '79':
   print("KİLİS")
elif plaka == '80':
   print("OSMANİYE")
elif plaka == '81':
   print("DÜZCE")

saat = int(input("KALDIĞINIZ SÜREYİ GİRİNİZ:"))

ücret = 0

if saat <= 1:
  ücret = 5
elif saat <= 5:
  ücret = 4 * saat
else:
  ücret = 3 * saat

print("ÖDEMENİZ GEREKEN ÜCRET :{}".format(ücret)) 

araç="06 AAB 4356","34 AGH 5687","47 MRD 4734" 
hasar = str(input("lütfen araç plakanızı giriniz:"))

if hasar =="06 AAB 4356":
   print("hasar yok")
    
elif hasar =="34 AGH 5687":
   print("hasar %25 vardır.")

elif hasar =="47 MRD 4734":    
   print("hasar %75 vardır.lütfen arabanın bakımını yapınız.")
    
bilgi = str(input("lütfen tekrar araç plakanızı giriniz:"))

if bilgi =="06 AAB 4356":
   print("10.000 km , dizel , otomatik , 2017 model")
    
elif bilgi =="34 AGH 5687":
   print("100.000 km , benzin , manuel , 2007 model")
    
elif bilgi =="47 MRD 4734":
   print("213.000 km , benzin , manuel , 2000 model")
   
iller="istanbul","ankara","mardin","izmir","kocaeli"
trafik="çok fazla","fazla","orta","iyi"

il = str(input("lütfen ili yazınız: "))

if il =="istanbul":
   print("trafik çok fazla")
   
elif il =="ankara":
   print("trafik orta")

elif il =="mardin":
   print("trafik iyi")

elif il =="izmir":
   print("trafik orta")

elif il =="kocaeli":
   print("trafik fazla")   

metin ="python"

print(len(metin))

liste =[2,36,"python",2,5]

print(len(liste))

for sayi in range(20):
 
    if sayi%2==0:
       
        continue
       
    else:
    
         print(sayi)
         