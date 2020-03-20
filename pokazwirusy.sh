#!/bin/bash
wget -O pokazwirusy.dane http://pokazwirusa.pl
cat pokazwirusy.dane | grep "var woj1" > pokazwirusy.linia
python3 pokazwirusy.py
