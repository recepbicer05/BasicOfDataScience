# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız

text = "The goal is to turn data into information, and information into insight"
print(text.upper().replace(","," ").replace("."," ").split())

#Verilen listeye aşağıdaki adımları uygulayınız.
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

print(len(lst))
print(lst[0],lst[10])

new_lst = lst[0:4]
print(new_lst)

lst.pop(8) #silmek için
print(lst)

lst.append(21)
print(lst)

lst.insert(8, "N")
print(lst)

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# Adım 1: Key değerlerine erişiniz.
# Adım 2: Value'lara erişiniz.
# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım 5: Antonio'yu dictionary'den siliniz.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

print(dict.keys())
print(dict.values())

dict.update({'Daisy': ["England", 13]})
print(dict)

dict.update({'Ahmet': ["Turkey", 24]})
print(dict)

dict.pop("Antonio")
print(dict)

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def divide_numbers(l):
    odd = []
    even = []
    for index in l:
        if index % 2 == 0:
           even.append(index)
        else:
           odd.append(index)

    print(odd,even)
    return odd, even

divide_numbers(l)


# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, x in enumerate(ogrenciler):
    if i<3:
            i += 1
            print("Mühendislik Fakültesi",i, ". öğrenci: ",x)
    else:
            i -= 2
            print("Tıp Fakültesi",i,". öğrenci: ",x)

# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
        print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


# Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
        if set1.issuperset(set2):
                print(set1.intersection(set2))
        else:
                print(set2.difference(set1))

kume(kume1,kume2)
kume(kume2,kume1)