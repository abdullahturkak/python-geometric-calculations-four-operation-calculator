import modulx
while True:
    try:
        secim=int(input("Hesap makinesi için 1 \nGeometrik şekiller için 2'e basınız\nÇıkış yapmak için 0'ye basınız\n"))
        if secim==1:
            hesap=int(input("Toplama = 1\nÇıkarma = 2\nÇarpma = 3\nBölme = 4\n"))
            if hesap==1:
                modulx.topla()
            elif hesap==2:
                modulx.cıkar()
            elif hesap==3:
                modulx.carp()
            elif hesap==4:
                modulx.bol()
            else:
                print("geçersiz değer")
            ##kare 
        elif secim==2:
                sekil=int(input("Kare'nin alanı ve çevresi=1\nDikdörtgen'nin alanı ve çevresi= 2\nÜçgen'nin alanı ve çevresi= 3\n"))
                if sekil == 1:
                            modulx.kare()
            ##dikdörtgen   
                elif sekil == 2:
                        modulx.dikdortgen()

            ##üçgen  
                elif sekil == 3:
                        modulx.ucgen()
                else:
                        print("geçersiz değer")
        elif secim==0:
                print("Çıkış yaptınız")
                break
        else:
                print("Yanlış değer girdiniz")
                break
    except (ValueError,ZeroDivisionError):
        print("Lütfen Belirtilen Değer Giriniz")
