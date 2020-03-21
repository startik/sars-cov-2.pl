# sars-cov-2.pl
Skrypt do wyciągania statystyk zakażeń na SARS-CoV-2 ze strony Ministerstwa Zdrowia:

https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2

(wyciąganie ze strony pokazwirusa.pl zostało zaniechane - strona posiada opóźnienie w stosunku do danych z Ministerstwa)

Sposób użycia (zalecane uruchomienie cykliczne, np. co 5 minut, przy pomocy Crontab'a):

./gov.sh

Aplikacja wysyła po wykryciu aktualizacji przy pomocy Pushover. W pierwszych liniach gov.py miejsce api_token i user_token należy podać klucz API aplikacji w Pushover i klucz użytkownika.

Aplikacja domyślnie raportuje województwo numer 5 (licząc od 0, alfabetycznie), czyli małopolskie. Aby zmienić - należy zmienić numer województwa (Zamiast [5]) w linii:

wiadomosc += "{}: {} / {}\n".format(lista[5][0],lista[5][1],lista[5][2])
