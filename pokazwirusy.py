import re

plik = open("pokazwirusy.linia","r")
linia = plik.read()
lista=[]
for x in re.split("'; +var",linia):
 numer = re.search("woj([0-9]+) ",x)
 numer = numer.group(1)
 woj = re.search("<h2>(.*)</h2>",x)
 woj = woj.group(1)
 liczby = re.search("<b>Razem</b><br> +Zakażeń:(.*)<b>([0-9]+)</b>(.*)Zgonów:(.*)<b>([0-9]+)</b>",x)
 zakazen = liczby.group(2)
 zgonow = liczby.group(5)
 lista.append([int(numer),woj,int(zakazen),int(zgonow)])

sumazakazen=0
sumazgonow=0
for wpis in lista:
 print ("{}: {} ({}/{})".format(wpis[0],wpis[1],wpis[2],wpis[3]))
 sumazakazen += wpis[2]
 sumazgonow += wpis[3]
print ()
print ("W sumie: {} zakażeń i {} zgonów".format(sumazakazen,sumazgonow))

krakow_wpis = re.search("<b>Kraków</b><br>Zakażeń: +([0-9]+) +Zgonów: +([0-9]+)",linia)
krakow_zakazen = int(krakow_wpis.group(1))
krakow_zgonow = int(krakow_wpis.group(2))
print ()
print ("W Krakowie: {} zakażeń i {} zgonów".format(krakow_zakazen,krakow_zgonow))
