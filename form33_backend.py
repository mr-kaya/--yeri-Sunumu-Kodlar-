from flask import Flask,jsonify,make_response,request, CORS, cross_origin, MySQL, OrderDict

import random
app = Flask(__name__)

mysql = MySQL(app)
cors = CORS(app)


def writeToDatabase(gelenData):
        item=[] 

        form_adi=gelenData["formAdi"]

        for key in gelenData.keys():
            item.append(key.split("[]")[0])

        if form_adi =="from33":
            try:
                user_id=random.randint(1,679959959)
                toplantiyeri=str(gelenData["toplantiyeri"]) if "toplantiyeri" in gelenData.keys() else ""
                toplantitarihi=str(gelenData["toplantitarihi"]) if "toplantitarihi" in gelenData.keys() else ""
                toplantisaati=str(gelenData["toplantisaati"]) if "toplantisaati" in gelenData.keys() else ""
                abdbaskaniadi=gelenData["abdbaskaniadi"] if "abdbaskaniadi" in gelenData.keys() else ""
                abdbaskanisoyadi=gelenData["abdbaskanisoyadi"] if "abdbaskanisoyadi" in gelenData.keys() else ""
                ogrenciadi=gelenData["ogrenciadi"] if "ogrenciadi" in gelenData.keys() else ""
                ogrencisoyadi=gelenData["ogrencisoyadi"] if "ogrencisoyadi" in gelenData.keys() else ""
                ogrencino=gelenData["ogrencino"] if "ogrencino" in gelenData.keys() else ""
                ogrencikayittarihi=str(gelenData["ogrencikayittarihi"]) if "ogrencikayittarihi" in gelenData.keys() else ""
                birinciogretimuyesininadi=gelenData["birinciogretimuyesininadi"] if "birinciogretimuyesininadi" in gelenData.keys() else ""
                birinciogretimuyesininsoyadi=gelenData["birinciogretimuyesininsoyadi"] if "birinciogretimuyesininsoyadi" in gelenData.keys() else ""
                ikinciogretimuyesininadi=gelenData["ikinciogretimuyesininadi"] if "ikinciogretimuyesininadi" in gelenData.keys() else ""
                ikinciogretimuyesininsoyadi=gelenData["ikinciogretimuyesininsoyadi"] if "ikinciogretimuyesininsoyadi" in gelenData.keys() else ""
                ucuncuogretimuyesininadi=gelenData["ucuncuogretimuyesininadi"] if "ucuncuogretimuyesininadi" in gelenData.keys() else ""
                ucuncuogretimuyesininsoyadi=gelenData["ucuncuogretimuyesininsoyadi"] if "ucuncuogretimuyesininsoyadi" in gelenData.keys() else ""
                birinciogretimuyesininepostasi=gelenData["birinciogretimuyesininepostasi"] if "birinciogretimuyesininepostasi" in gelenData.keys() else ""
                tikuyeleritarih1=str(gelenData["tikuyeleritarih1"]) if "tikuyeleritarih1" in gelenData.keys() else ""
                ikinciogretimuyesininepostasi=gelenData["ikinciogretimuyesininepostasi"] if "ikinciogretimuyesininepostasi" in gelenData.keys() else ""
                tikuyeleritarih2=str(gelenData["tikuyeleritarih2"]) if "tikuyeleritarih2" in gelenData.keys() else ""
                ucuncuogretimuyesininepostasi=gelenData["ucuncuogretimuyesininepostasi"] if "ucuncuogretimuyesininepostasi" in gelenData.keys() else ""
                tikuyeleritarih3=str(gelenData["tikuyeleritarih3"]) if "tikuyeleritarih3" in gelenData.keys() else ""
                programiniz=gelenData["programiniz"] if "programiniz" in gelenData.keys() else ""
                birinciogretimuyesininunvani=gelenData["birinciogretimuyesininunvani"] if "birinciogretimuyesininunvani" in gelenData.keys() else ""
                ikinciogretimuyesininunvani=gelenData["ikinciogretimuyesininunvani"] if "ikinciogretimuyesininunvani" in gelenData.keys() else ""
                ucuncuogretimuyesininunvani=gelenData["ucuncuogretimuyesininunvani"] if "ucuncuogretimuyesininunvani" in gelenData.keys() else ""
                birinciogretimuyesininkurumu=gelenData["birinciogretimuyesininkurumu"] if "birinciogretimuyesininkurumu" in gelenData.keys() else ""
                ikinciogretimuyesininkurumu=gelenData["ikinciogretimuyesininkurumu"] if "ikinciogretimuyesininkurumu" in gelenData.keys() else ""
                ucuncuogretimuyesininkurumu= gelenData["ucuncuogretimuyesininkurumu"] if "ucuncuogretimuyesininkurumu" in gelenData.keys() else ""
                bilimdali=gelenData["bilimdali"] if "bilimdali" in gelenData.keys() else ""
                danismanad=gelenData["danismanad"] if "danismanad" in gelenData.keys() else ""
                danismansoyad=gelenData["danismansoyad"] if "danismansoyad" in gelenData.keys() else ""
                abdbaskaniUnvani=gelenData["abdbaskaniUnvani"] if "abdbaskaniUnvani" in gelenData.keys() else ""


        cursor = mysql.connection.cursor()
        sorgu33="INSERT INTO form33 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu33,(user_id, toplantiyeri, toplantitarihi, toplantisaati, abdbaskaniadi, abdbaskanisoyadi,
                        abdbaskaniUnvani, programiniz, 
                        birinciogretimuyesininadi, ikinciogretimuyesininadi, ucuncuogretimuyesininadi,
                        birinciogretimuyesininsoyadi, ikinciogretimuyesininsoyadi, ucuncuogretimuyesininsoyadi,
                        birinciogretimuyesininunvani, ikinciogretimuyesininunvani, ucuncuogretimuyesininunvani,
                        birinciogretimuyesininkurumu, ikinciogretimuyesininkurumu, ucuncuogretimuyesininkurumu,
                        birinciogretimuyesininepostasi, ikinciogretimuyesininepostasi, ucuncuogretimuyesininepostasi,
                        tikuyeleritarih1, tikuyeleritarih2, tikuyeleritarih3))
          
        mysql.connection.commit()
        cursor.close()


        cursor = mysql.connection.cursor()
        ogrenci_bilgileri="INSERT INTO ogrenciBilgileri  VALUES(%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(ogrenci_bilgileri,(user_id, ogrenciadi, ogrencisoyadi, ogrencino,
                                bilimdali, danismanad, danismansoyad))
        mysql.connection.commit()
        cursor.close()




        