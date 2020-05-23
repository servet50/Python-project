import requests
from bs4 import BeautifulSoup

print(" HOŞGELDİNİZ ")

while True:

    print(""""
                                    [1] Türkiyedeki En İyi Filmler
                                    [2] Dünyadaki En İyi Filmler
                                    [Q] Çıkış
                                    """)
    secim2 = input("İşleminiz: ")


    if secim2 == "1":


        url = "https://boxofficeturkiye.com/hafta/?yil=2018&hafta=7"

        headers_param = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}


        r = requests.get(url,headers = headers_param)

        soup = BeautifulSoup(r.content,"lxml")

        filmTablosu = soup.find("table",attrs={"class":"ustcizgi"}).select("tr:nth-of-type(2) > td > table:nth-of-type(3) > tr")
        for i in range (1,21):
                    filmAdi = filmTablosu[i].find("a",attrs={"class":"film"}).get("title")

                    toplamSeyirci = filmTablosu[i].select("td:nth-of-type(10) > font")[0].text

                    hasilat = filmTablosu[i].select("td:nth-of-type(9) > font")[0].text

                    print("Film Adı: {} \nHasılat: {} \nToplam Seyirci: {}".format(filmAdi,hasilat,toplamSeyirci))

    elif secim2=="2":

                imdburl = "https://www.imdb.com/chart/top"

                r = requests.get(imdburl)

                soup = BeautifulSoup(r.content, "lxml")

                gelen_veri = soup.find_all("table", {"class": "chart full-width"})

                ffilmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents) - 2]

                ffilmtablosu = ffilmtablosu.find_all("tr")

                for ffilm in ffilmtablosu:

                    ffilmbasliklari = ffilm.find_all("td", {"class": "titleColumn"})

                    ffilmismi = ffilmbasliklari[0].text

                    ffilmismi = ffilmismi.replace("\n", "")

                    print(ffilmismi)

                    print("***********************")

    else:
        break