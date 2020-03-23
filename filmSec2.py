import xlrd
wb = xlrd.open_workbook(r"C:\Users\Selahattin\Desktop\Book1.xlsx")   #Excel dosyasını nereye koyarsan oranın dosya yolunu buraya yapıştır.
sh1 = wb.sheet_by_index(0) # first sheet in workbook
col = sh1.col_values(0)

#print ("Sheet1", sh1.name) # name of sheet
#for rownum in range(sh1.nrows): # sh1.nrows -> number of rows (ncols -> num columns)
    #print(sh1.row_values(rownum))
    #print(sh1.cell(rowx=2,colx=2).value)

def programi_baslat():
    baslat = 0
    baslat = int(input("Film Önerme Aracını başlatmak için lütfen 1'e basınız, Çıkış için ise 0'a basınız: "))
    if baslat == 0:
        print("Başarıyla çıkış yaptınız.")
        return 0
    elif baslat == 1:
        print("Şimdi senin için bir film seçeceğim, hazır mısın?\n")
        return ready_or_not()
    else:
        print("Lütfen geçerli bir değer girer misin?\n")
        return programi_baslat()

def random_film_sec():
    import random
    print("Bugün sana izlemen için önereceğim film taaam olarak şu ---->", random.choice(col))
    print(" ")
    bunu_izledim()

def ready_or_not():
    ready = 0
    ready = int(input("Eğer hazırsan 1'e, değilsen 0'a basabilirsin: "))
    if ready == 0:
        print("Peekala ne zaman hazır hissedersen. Seni ana menüye yönlendiriyorum!\n")
        return programi_baslat()
    elif ready == 1:
        return random_film_sec()
    else:
        print("Lütfen geçerli bir değer girer misin?\n")
        return ready_or_not()

def bunu_izledim():
    aw = 0
    aw = str(input("Eğer daha önce bu filmi izlediysen tekrar seçmeyi deneyebilirim. (Sec - Secme)"))
    if aw == 'Secme':
        print("O zaman iyi seyirler :D")
        return 0
    elif aw == 'Sec':
        print("Hemen yeni bir film seçiyorum: ")
        return random_film_sec()
    else:
        print("Lütfen geçerli bir değer giriniz...")
        return bunu_izledim()

#print('"A" column content:')
#for cell in col:
     #print(cell)
#print (sh1.col_values(1))


# MAIN

print("******************************** IMDB EN İYİ 250 FİLM ÖNERME ARACINA HOŞGELDİNİZ! ********************************")
print("           ********************************                            ********************************")
print("                  ************************************       ********************************")
print("                                                      *******\n")

programi_baslat()
