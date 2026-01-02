import isi
import random
import renk
#GEREKLİ KÜTÜPHANELER İNDİRİLDİ#
def sifre():
    kelime = input("Bir sözcük/cümle giriniz ")
    #KULLANICIDAN CÜMLE ALINDI#
    sira = 0 
    metin = ""
    #GEREKLİ DEĞİŞKENLER OLUŞTURULDU#
    while sira < len(kelime):
        if kelime[sira] == "a" or kelime[sira] == "A":
            metin += isi.a
        elif kelime[sira] == "b" or kelime[sira] == "B":
            metin += isi.b
        elif kelime[sira] == "c" or kelime[sira] == "C":
            metin += isi.c
        elif kelime[sira] == "ç" or kelime[sira] == "Ç":
            metin += isi.ch
        elif kelime[sira] == "d" or kelime[sira] == "D":
            metin += isi.d
        elif kelime[sira] == "e" or kelime[sira] == "E":
            metin += isi.e
        elif kelime[sira] == "f" or kelime[sira] == "F": 
            metin += isi.f
        elif kelime[sira] == "g" or kelime[sira] == "G":
            metin += isi.g
        elif kelime[sira] == "ğ" or kelime[sira] == "Ğ":
            metin += isi.gh
        elif kelime[sira] == "h" or kelime[sira] == "H":
            metin += isi.h
        elif kelime[sira] == "ı" or kelime[sira] == "I":
            metin += isi.i
        elif kelime[sira] == "i" or kelime[sira] == "İ":
            metin += isi.ii
        elif kelime[sira] == "j" or kelime[sira] == "J":
            metin += isi.j
        elif kelime[sira] == "k" or kelime[sira] == "K":
            metin += isi.k
        elif kelime[sira] == "l" or kelime[sira] == "L":
            metin += isi.l
        elif kelime[sira] == "m" or kelime[sira] == "M":
            metin += isi.m
        elif kelime[sira] == "n" or kelime[sira] == "N":
            metin += isi.n
        elif kelime[sira] == "o" or kelime[sira] == "O":
            metin += isi.o
        elif kelime[sira] == "ö" or kelime[sira] == "Ö":
            metin += isi.oh
        elif kelime[sira] == "p" or kelime[sira] == "P":
            metin += isi.p
        elif kelime[sira] == "r" or kelime[sira] == "R":
            metin += isi.r
        elif kelime[sira] == "s" or kelime[sira] == "S":
            metin += isi.s
        elif kelime[sira] == "ş" or kelime[sira] == "Ş":
            metin += isi.sh
        elif kelime[sira] == "t" or kelime[sira] == "T": 
            metin += isi.t
        elif kelime[sira] == "u" or kelime[sira] == "U":
            metin += isi.u
        elif kelime[sira] == "ü" or kelime[sira] == "Ü":
            metin += isi.uh
        elif kelime[sira] == "v" or kelime[sira] == "V":
            metin += isi.v
        elif kelime[sira] == "y" or kelime[sira] == "Y":
            metin += isi.y
        elif kelime[sira] == "z" or kelime[sira] == "Z":
            metin += isi.z
        elif kelime[sira] == " ":
            metin += isi.null
        elif kelime[sira] == ",":
            metin += isi.virgul
        elif kelime[sira] == ".":
            metin += isi.nokta
        elif kelime[sira] == ":":
            metin += isi.ikinokta
        elif kelime[sira] == "?":
            metin += isi.soru
        elif kelime[sira] == "!":
            metin += isi.unlem
        elif kelime[sira] == "0":
            metin += isi.sifir
        elif kelime[sira] == "1":
            metin += isi.bir
        elif kelime[sira] == "2":
            metin += isi.iki
        elif kelime[sira] == "3":
            metin += isi.uc
        elif kelime[sira] == "4":
            metin += isi.dort
        elif kelime[sira] == "5":
            metin += isi.bes
        elif kelime[sira] == "6":
            metin += isi.alti
        elif kelime[sira] == "7":
            metin += isi.yedi
        elif kelime[sira] == "8":
            metin += isi.sekiz
        elif kelime[sira] == "9":
            metin += isi.dokuz
        else:
            pass
        sira += 1
    #METİN ISI KODLARINA GÖRE ŞİFRELENDİ#
    print("ISIYA GÖRE ŞİFRELENMİŞ METİN: " + metin)
    #ŞİFRELENMİŞ METİN YAZDIRILDI#
    basamak = 0
    a = []
    anahtar_kod = ""
    while basamak < len(kelime) * 2:
            a.append(str(random.randint(0, 9)))
            basamak += 1
    basamak = 0
    for i in range(len(kelime) * 2):
        anahtar_kod += a[basamak]    
        basamak += 1
    #ANAHTAR KOD OLUŞTURULDU#
    print("ANAHTAR KOD:" + anahtar_kod)
    #ANAHTAR KOD YAZDIRILDI#
    sonuc = []
    for i in range(len(anahtar_kod)):
        harf = int(metin[i * 2]) + int(anahtar_kod[i])
        sonuc.append(harf)
    print("TOPLAMLAR:" + str(sonuc))
    modlar = []
    for i in range(len(sonuc)):
        mod = sonuc[i] % 10
        modlar.append(mod)
    print("MODLAR:" + str(modlar) + " (ISI ŞİFRESİ)")
    isisifresi = str(modlar)
    #ISIYA GÖRE ŞİFRELENDİ#
    sira = 0 
    metin = ""
    #GEREKLİ DEĞİŞKENLER OLUŞTURULDU#
    while sira < len(kelime):
        if kelime[sira] == "a" or kelime[sira] == "A":
            metin += renk.a
        elif kelime[sira] == "b" or kelime[sira] == "B":
            metin += renk.b
        elif kelime[sira] == "c" or kelime[sira] == "C":
            metin += renk.c
        elif kelime[sira] == "ç" or kelime[sira] == "Ç":
            metin += renk.ch
        elif kelime[sira] == "d" or kelime[sira] == "D":
            metin += renk.d
        elif kelime[sira] == "e" or kelime[sira] == "E":
            metin += renk.e
        elif kelime[sira] == "f" or kelime[sira] == "F": 
            metin += renk.f
        elif kelime[sira] == "g" or kelime[sira] == "G":
            metin += renk.g
        elif kelime[sira] == "ğ" or kelime[sira] == "Ğ":
            metin += renk.gh
        elif kelime[sira] == "h" or kelime[sira] == "H":
            metin += renk.h
        elif kelime[sira] == "ı" or kelime[sira] == "I":
            metin += renk.i
        elif kelime[sira] == "i" or kelime[sira] == "İ":
            metin += renk.ii
        elif kelime[sira] == "j" or kelime[sira] == "J":
            metin += renk.j
        elif kelime[sira] == "k" or kelime[sira] == "K":
            metin += renk.k
        elif kelime[sira] == "l" or kelime[sira] == "L":
            metin += renk.l
        elif kelime[sira] == "m" or kelime[sira] == "M":
            metin += renk.m
        elif kelime[sira] == "n" or kelime[sira] == "N":
            metin += renk.n
        elif kelime[sira] == "o" or kelime[sira] == "O":
            metin += renk.o
        elif kelime[sira] == "ö" or kelime[sira] == "Ö":
            metin += renk.oh
        elif kelime[sira] == "p" or kelime[sira] == "P":
            metin += renk.p
        elif kelime[sira] == "r" or kelime[sira] == "R":
            metin += renk.r
        elif kelime[sira] == "s" or kelime[sira] == "S":
            metin += renk.s
        elif kelime[sira] == "ş" or kelime[sira] == "Ş":
            metin += renk.sh
        elif kelime[sira] == "t" or kelime[sira] == "T": 
            metin += renk.t
        elif kelime[sira] == "u" or kelime[sira] == "U":
            metin += renk.u
        elif kelime[sira] == "ü" or kelime[sira] == "Ü":
            metin += renk.uh
        elif kelime[sira] == "v" or kelime[sira] == "V":
            metin += renk.v
        elif kelime[sira] == "y" or kelime[sira] == "Y":
            metin += renk.y
        elif kelime[sira] == "z" or kelime[sira] == "Z":
            metin += renk.z
        elif kelime[sira] == " ":
            metin += renk.null
        elif kelime[sira] == ",":
            metin += renk.virgul
        elif kelime[sira] == ".":
            metin += renk.nokta
        elif kelime[sira] == ":":
            metin += renk.ikinokta
        elif kelime[sira] == "?":
            metin += renk.soru
        elif kelime[sira] == "!":
            metin += renk.unlem
        elif kelime[sira] == "0":
            metin += renk.sifir
        elif kelime[sira] == "1":
            metin += renk.bir
        elif kelime[sira] == "2":
            metin += renk.iki
        elif kelime[sira] == "3":
            metin += renk.uc
        elif kelime[sira] == "4":
            metin += renk.dort
        elif kelime[sira] == "5":
            metin += renk.bes
        elif kelime[sira] == "6":
            metin += renk.alti
        elif kelime[sira] == "7":
            metin += renk.yedi
        elif kelime[sira] == "8":
            metin += renk.sekiz
        elif kelime[sira] == "9":
            metin += renk.dokuz
        else:
            pass
        sira += 1
    #METİN RENK KODLARINA GÖRE ŞİFRELENDİ#
    print("RENGE GÖRE ŞİFRELENMİŞ METİN: " + metin)
    #ŞİFRELENMİŞ METİN YAZDIRILDI#
    print("ANAHTAR KOD:" + anahtar_kod)
    sonuc = []
    for i in range(len(anahtar_kod)):
        harf = int(metin[i * 2]) + int(anahtar_kod[i])
        sonuc.append(harf)
    print("TOPLAMLAR:" + str(sonuc))
    modlar = []
    for i in range(len(sonuc)):
        mod = sonuc[i] % 10
        modlar.append(mod)
    print("MODLAR:" + str(modlar) + " (RENK ŞİFRESİ)")
    renksifresi = str(modlar)
    #RENGE GÖRE ŞİFRELENDİ#
    with open("anahtar_kod.txt", "w", encoding="utf-8") as f:
        f.write(anahtar_kod)
    with open("isisifresi.txt", "w", encoding="utf-8") as f:
        f.write(isisifresi)
    with open("renksifresi.txt", "w", encoding="utf-8") as f:
        f.write(renksifresi)
    #DEĞİŞKENLER KOPYALANDI#
