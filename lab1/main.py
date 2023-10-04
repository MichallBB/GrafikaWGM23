import numpy as np
from PIL import Image


obrazek = Image.open("mb.bmp")
print("tryb: ", obrazek.mode)
print("rozmiar: ", obrazek.size)
print("format: ", obrazek.format)

dane_obrazka = np.asarray(obrazek)
dane_obrazka1 = dane_obrazka * 1

# zad 3
# zapis tablicy do pliku
t1_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')
t1_text.close()

# Zad 4
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",dane_obrazka.itemsize)
print("wyraz (49,30):", dane_obrazka[30][49])
print("wyraz (90,40):", dane_obrazka[40][90])
print("wyraz (99,0):", dane_obrazka[0][99])
print("************************\n")
# Zad 5
t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
print("typ danych tablicy t1:", t1.dtype)
print("rozmiar tablicy t1 :", t1.shape)
print("wymiar tablicy t1 :", t1.ndim)

# Zad 6
t3 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("\ntyp danych tablicy t3:", t3.dtype)
print("rozmiar tablicy t3 :", t3.shape)
print("wymiar tablicy t3 :", t3.ndim)

# Obraz wyjściowy jest cały czarny dlatego że elementy mają wartość 0 lub 1,
# a wartość kodu koloru zmieniła się na zakres od 0 do 255 przy czym 255 to biały a 0 to czarny
obraz = Image.fromarray(t3)
obraz.show()
