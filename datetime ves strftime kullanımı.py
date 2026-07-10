import datetime
import locale
#tarih bilgilerinin biçimlendirilmesi,strnge dönüştürülmesi
#strftime()
an=datetime.datetime.now()
print(an)
print(an.strftime("%Y"))#yil
print(an.strftime("%X"))#saat
print(an.strftime("%d"))#gün ayın kaçıncı günü
print(an.strftime("%A"))#gün ismi
print(an.strftime("%B"))#ay ismi
# taih saat bilgisini yerel(local) bilgisibe dönüştürme
locale.setlocale(locale.LC_ALL,'tr_TR.UTF-8')
an2=datetime.datetime.now()
print(an2)
print(an2.strftime("%Y"))#yil
print(an2.strftime("%X"))#saat
print(an2.strftime("%d"))#gün ayın kaçıncı günü
print(an2.strftime("%A"))#gün ismi
print(an2.strftime("%B"))#ay ismi

print(an2.strftime('%d %B %Y'))
print(an2.strftime('%d.%B.%Y'))
