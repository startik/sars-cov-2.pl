#!/bin/bash
cd /home/dasiu/sars-cov-2.pl
wget -O gov.dane https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2
cat gov.dane | grep "<pre id=\"registerData\"" > gov-linia1.txt
date >> gov.log
python3 gov.py >> gov.log
