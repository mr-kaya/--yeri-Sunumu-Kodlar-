sorgu7 = "INSERT INTO tezBilgiler31 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.execute(sorgu7,(tezTurkce, tezIngilizce, tezAmac, tezTanim, tezHipotez, tezMotivasyon, konudetay, literatur, yontem, Ozgun, Yaygin, Kurum))

sorgu8 = "INSERT INTO tikUyeleri33 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.execute(sorgu8,( birinciogretimuyesininadi, ikinciogretimuyesininadi, ucuncuogretimuyesininadi, birinciogretimuyesininsoyadi, ikinciogretimuyesininsoyadi, ucuncuogretimuyesininsoyadi, birinciogretimuyesininunvani, ikinciogretimuyesininunvani, ucuncuogretimuyesininunvani, birinciogretimuyesininkurumu, ikinciogretimuyesininkurumu, ucuncuogretimuyesininkurumu, birinciogretimuyesininepostasi, ikinciogretimuyesininepostasi, ucuncuogretimuyesininepostasi, tikuyeleritarih1, tikuyeleritarih2, tikuyeleritarih3 ))

sorgu9 = "INSERT INTO toplantiBilgiler33 VALUES(%s, %s)"
cursor.execute(sorgu9,(toplantiyeri, toplantitarihivesaati))

#Form 34
form34_ogr_bilgileri = "INSERT INTO ogrenciBilgileri VALUES(%s, %s, %d, %s, %s, %s)"
cursor.execute(form34_ogr_bilgileri,(ad, soyad, ogrenciNo, bilimdali, danismanad, danismansoyad))

#/Form 34 ögrenci bilgileri başlığındaki sıkıntılar.
# 1. Kayıt tarihi diye alan bırakılmış. Ama ne ogrenci bilgilerinde 
# ne de form34 tablosunda alanı yok.,
# 2. Tez danışmanı, kişinin normal danışmanı mıdır? 
# Normal danışmanı ise, formdaki Tez danışman boşluğuna
# danışmanın ismi mi yoksa soyismi mi yazılmalı. 
# Yani doldurulması gereken 1 yer var iken database'de ad ve soyad olarak 
# 2 yer var. Bunun kodda ayrıştırılması lazım.
#/#