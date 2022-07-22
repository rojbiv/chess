deger=(1, 64)
deger=int(input("bir değer giriniz: "))
while(deger<=0):
   deger=int(input("Lütfen sıfır ya da sıfırdan büyük bir değer giriniz... "))

x_ekseni=8
y_ekseni=8

x_koordinat=deger%x_ekseni


if x_koordinat==0:
    x_koordinat=x_ekseni
if deger%y_ekseni==0:
    y_koordinat=int(deger%y_ekseni)
else: 
    y_koordinat=int(deger%y_ekseni)+1

print(x_koordinat)
print(y_koordinat)

#at için 
x=(1,9)
y=(1,9)

At=[]
At.append((x + 2, y - 1))
At.append((x + 2, y + 1))
At.append((x - 2, y + 1))
At.append((x - 2, y - 1))
At.append((x + 1, y + 2))
At.append((x + 1, y - 2))
At.append((x - 1, y + 2))
At.append((x - 1, y - 2))     

 
