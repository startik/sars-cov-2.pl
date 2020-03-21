import re
import requests
import urllib

api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
user_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

plik = open("gov-linia1.txt","r")
linia = plik.read()
plik.close()
lista=[]

aktualizacja_search = re.search('aktualne na +: +([0-9]+\.[0-9]+\.[0-9]+ +[0-9]+:[0-9]+)"',linia)
aktualizacja = aktualizacja_search.group(1)
suma = aktualizacja + ";"

linia_zero = 1
print (aktualizacja)

for x in re.split('\\{\\\\"Województwo\\\\":',linia):
 if linia_zero == 0:
  dane = re.search('\\\\"(.*)\\\\",\\\\"Liczba\\\\":\\\\"(.*)\\\\",\\\\"Liczba zgonów\\\\":\\\\"(.*)\\\\",',x)
  woj = dane.group(1)
  zakazen = dane.group(2)
  zgonow = dane.group(3)
  if zakazen == "":
   zakazen=0
  if zgonow == "":
   zgonow=0
  if woj == "Cała Polska":
   suma_zakazen_check = int(zakazen)
   suma_zgonow_check = int(zgonow)
  else:
   lista.append([woj,int(zakazen),int(zgonow)])
 else:
  linia_zero=0

sumazakazen=0
sumazgonow=0
for wpis in lista:
 print ("{}: {} / {}".format(wpis[0],wpis[1],wpis[2]))
 suma = suma + "{};{};{};".format(wpis[0],wpis[1],wpis[2])
 sumazakazen += wpis[1]
 sumazgonow += wpis[2]

print ("W sumie policzono: {} zakażeń i {} zgonów. Rząd podaje sumy {} i {}.".format(sumazakazen,sumazgonow,suma_zakazen_check,suma_zgonow_check))
print ("Dane aktualizowane {}".format(aktualizacja))

plik_suma = open("gov-suma.txt","r")
stara_suma = plik_suma.read()
plik_suma.close()
if suma != stara_suma:
 print ("Jest zmiana, zapisujemy i wysyłamy!")
 plik_suma = open("gov-suma.txt","w")
 plik_suma.write(suma)
 plik_suma.close()
 plik_historia = open("gov-historia.txt","a+")
 plik_historia.write("\n{}".format(suma))
 plik_historia.close()
 wiadomosc = "Aktualizacja z {}:\n".format(aktualizacja)
 wiadomosc += "Polska: {} / {}\n".format(sumazakazen,sumazgonow)
 wiadomosc += "{}: {} / {}\n".format(lista[5][0],lista[5][1],lista[5][2])
 print (wiadomosc)
 json_data = {"token":api_token, "user":user_token, "message":wiadomosc}
 json_data_encoded = urllib.parse.urlencode(json_data)
 requests.post("https://api.pushover.net/1/messages.json", data = json_data_encoded)
dasiu@ubuntu-cloud:~/sars-cov-2.pl$ nano gov.py
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$ cat gov.sh
#!/bin/bash
cd /home/dasiu/sars-cov-2.pl
wget -O gov.dane https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2
cat gov.dane | grep "<pre id=\"registerData\"" > gov-linia1.txt
date >> gov.log
python3 gov.py >> gov.log
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$
dasiu@ubuntu-cloud:~/sars-cov-2.pl$ cat gov.py
import re
import requests
import urllib

api_token = "aaqpw7rn3u7j652du6aig235tj3cs9"
user_token = "utgh2s3r1iyv11vq83zydyfn556scs"

plik = open("gov-linia1.txt","r")
linia = plik.read()
plik.close()
lista=[]

aktualizacja_search = re.search('aktualne na +: +([0-9]+\.[0-9]+\.[0-9]+ +[0-9]+:[0-9]+)"',linia)
aktualizacja = aktualizacja_search.group(1)
suma = aktualizacja + ";"

linia_zero = 1
print (aktualizacja)

for x in re.split('\\{\\\\"Województwo\\\\":',linia):
 if linia_zero == 0:
  dane = re.search('\\\\"(.*)\\\\",\\\\"Liczba\\\\":\\\\"(.*)\\\\",\\\\"Liczba zgonów\\\\":\\\\"(.*)\\\\",',x)
  woj = dane.group(1)
  zakazen = dane.group(2)
  zgonow = dane.group(3)
  if zakazen == "":
   zakazen=0
  if zgonow == "":
   zgonow=0
  if woj == "Cała Polska":
   suma_zakazen_check = int(zakazen)
   suma_zgonow_check = int(zgonow)
  else:
   lista.append([woj,int(zakazen),int(zgonow)])
 else:
  linia_zero=0

sumazakazen=0
sumazgonow=0
for wpis in lista:
 print ("{}: {} / {}".format(wpis[0],wpis[1],wpis[2]))
 suma = suma + "{};{};{};".format(wpis[0],wpis[1],wpis[2])
 sumazakazen += wpis[1]
 sumazgonow += wpis[2]

print ("W sumie policzono: {} zakażeń i {} zgonów. Rząd podaje sumy {} i {}.".format(sumazakazen,sumazgonow,suma_zakazen_check,suma_zgonow_check))
print ("Dane aktualizowane {}".format(aktualizacja))

plik_suma = open("gov-suma.txt","r")
stara_suma = plik_suma.read()
plik_suma.close()
if suma != stara_suma:
 print ("Jest zmiana, zapisujemy i wysyłamy!")
 plik_suma = open("gov-suma.txt","w")
 plik_suma.write(suma)
 plik_suma.close()
 plik_historia = open("gov-historia.txt","a+")
 plik_historia.write("\n{}".format(suma))
 plik_historia.close()
 wiadomosc = "Aktualizacja z {}:\n".format(aktualizacja)
 wiadomosc += "Polska: {} / {}\n".format(sumazakazen,sumazgonow)
 wiadomosc += "{}: {} / {}\n".format(lista[5][0],lista[5][1],lista[5][2])
 print (wiadomosc)
 json_data = {"token":api_token, "user":user_token, "message":wiadomosc}
 json_data_encoded = urllib.parse.urlencode(json_data)
 requests.post("https://api.pushover.net/1/messages.json", data = json_data_encoded)
