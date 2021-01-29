def topla():
    toplam=0
    while True:
        y=input("değer giriniz çıkış için c'ye basınız")
        if (y=="c"):
            print("program durdu",toplam)
            break
        else:
            y=int(y)
            toplam=toplam+y
            print(toplam)
def cıkar():
            cıkar='a'
            while True:
                    y=input("değer giriniz çıkış için c'ye basınız")
                    if (y=="c"):
                        print("program durdu",cıkar)
                        break
                    else:
                        y=int(y)
                    if(cıkar=='a'):
                        cıkar=int(y)
                    else:
                        cıkar-=y
                        print(cıkar)
            print(cıkar)
def carp():
            carpım=1
            while True:
                    y=input("değer giriniz çıkış için c'ye basınız")
                    if (y=="c"):
                        print("program durdu",carpım)
                        break
                    else:
                        y=int(y)
                    carpım*=y
                    print(carpım)
            print(carpım)
def bol():
            bol=0
            while True:
                    y=input("değer giriniz çıkış için c'ye basınız")
                    if (y=="c"):
                        print("program durdu",bol)
                        break
                    else:
                        y=float(y)
                    if(bol==0):
                        bol=y
                    else:
                        bol/=y
                    print(bol)
def kare():
    kare=int(input("Karenin alanı için= 1\nKarenin çevresi için= 2\n"))
    x= int(input("Kenarı gir = "))
    if (x==0 or y==0):
        print("yanlış değer girdiniz")
    elif kare==1:
        print("Karenin alanı= ",x**2)
    elif kare==2:
        print("Karenin çevresi= ",x*4)
    else:
        print("geçersiz değer")
def dikdortgen():
    dik=int(input("Dikdörtgenin alanı için= 1\ndikdörtgenin çevresi için= 2\n"))
    x= int(input("Uzun kenar gir = "))
    y= int(input("Kısa kenar gir = "))
    if dik==1:
        if(x<y or x==y or x==0 or y==0):
            print("yanlış değer girdiniz")
        else:
            print("Diktörtgenin alanı= ",x*y)
    elif dik==2:
        if(x<y or x==y or x==0 or y==0):
            print("yanlış değer girdiniz")
        else:
            print("Diktörtgenin çevresi= ",((x+y)*2))
    else:
        print("geçersiz değer")
def ucgen():
    üçgen=int(input("Üçgenin alanı için= 1\nÜçgenin çevresi için= 2\n"))
    x= int(input("Üçgenin bir kenarını gir = "))
    y= int(input("Üçgenin bir kenarını gir = "))
    z= int(input("Üçgenin bir kenarını gir = "))
    if (x==0 or y==0):
        print("yanlış değer girdiniz")
    elif üçgen==1:
        s=(x+y+z)/2
        print("Üçgenin alanı= ",int((s*(s-x)*(s-y)*(s-z))**0.5))
    elif üçgen==2:
        print("Üçgenin çevresi= ",int(x+y+z))
    else:
        print("geçersiz değer")


