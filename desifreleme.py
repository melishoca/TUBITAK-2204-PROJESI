import renk
import isi
import os
def desifreleme():
    if os.path.exists("anahtar_kod.txt"):
        with open("anahtar_kod.txt", "r", encoding="utf-8") as f:
            anahtar_kod = f.read()
        os.remove("anahtar_kod.txt")
    else:
        print("ANAHTAR KOD BULUNAMADI, LÜTFEN ÖNCE ŞİFRELEME PROGRAMINI ÇALIŞTIRIN.")
        return
    print("ANAHTAR KOD:" + anahtar_kod)
    if os.path.exists("isisifresi.txt"):
        with open("isisifresi.txt", "r", encoding="utf-8") as f:
            isisifresi = f.read()
        os.remove("isisifresi.txt")
    else:
        print("ISI ŞİFRESİ BULUNAMADI, LÜTFEN ÖNCE ŞİFRELEME PROGRAMINI ÇALIŞTIRIN.")
        return
    b = isisifresi.replace("," , "")
    b = b.replace("[" , "")
    b = b.replace("]" , "")
    b = b.replace(" ", "")
    print("ISI ŞİFRESİ:" + isisifresi)
    if os.path.exists("renksifresi.txt"):
        with open("renksifresi.txt", "r", encoding="utf-8") as f:
            renksifresi = f.read()
        os.remove("renksifresi.txt")
    else:
        print("RENK ŞİFRESİ BULUNAMADI, LÜTFEN ÖNCE ŞİFRELEME PROGRAMINI ÇALIŞTIRIN.")
        return
    c = renksifresi.replace("," , "")
    c = c.replace("[" , "")
    c = c.replace("]" , "")
    c = c.replace(" ", "")
    print("RENK ŞİFRESİ:" + renksifresi)
    isilar = []
    renkler = []
    #DEĞİŞKENLERİ ALMA#

    for i in range(len(anahtar_kod)):
        
        isiharf = int(b[i]) - int(anahtar_kod[i])
        if isiharf < 0:
            isiharf += 10
        isilar.append(isiharf)
        
    print("ISILAR:" + str(isilar))
    for i in range(len(anahtar_kod)):
        
        renkharf = int(c[i]) - int(anahtar_kod[i])
        if renkharf < 0:
            renkharf += 10
        renkler.append(renkharf)
        
    print("RENKLER:" + str(renkler))
    #ÇIKARMA DÖNGÜSÜ#
    j = str(isilar).replace("," , "")
    j = j.replace("[" , "")
    j = j.replace("]" , "")
    j = j.replace(" " , "")
    
    k = str(renkler).replace("," , "")
    k = k.replace("[" , "")
    k = k.replace("]" , "")
    k = k.replace(" " , "")
    #LİSTELER ARINDIRILDI#
  
    