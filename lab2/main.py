from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("inicjaly.bmp")  # wczytywanie obrazu

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", t_inicjaly.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka

# 1
def rysuj_ramke_w_obrazie(obraz, grub):
    obraz_wstawiany = np.asarray(obraz) * 1
    h, w = obraz_wstawiany.shape
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j] = 0
        for j in range(w - grub, w):
            obraz_wstawiany[i][j] = 0
    for i in range(w):
        for j in range(grub):
            obraz_wstawiany[j][i] = 0
        for j in range(h - grub, h):
            obraz_wstawiany[j][i] = 0
    tab = obraz_wstawiany.astype(bool)
    return Image.fromarray(tab)

# 2
tab = rysuj_ramke_w_obrazie(inicjaly, 10)
tab2 = rysuj_ramke_w_obrazie(inicjaly, 5)
tab2.save("ramka5.bmp")
tab.save("ramka10.bmp")

# 3
def rysuj_ramke(w, h, grub): # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    for j in range(int(min(w,h)/grub)):
        tab[j*grub:h - j*grub, j*grub:w - j*grub] = j % 2 # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    tab1 = tab.astype(np.bool_)
    return tab1

tab = rysuj_ramke(60, 120, 6)
tab2 = Image.fromarray(tab)
tab2.show()

# 3.1.2

def pionowe_paski(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile2 = int(w / grub)
    for k in range(ile2):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if(k % 2 == 1):
                    tab[j, i] = 1
    tab = tab * 255
    return Image.fromarray(tab)

tab = pionowe_paski(120, 60, 10)
print("typ danych tablicy", tab.size)
print("rozmiar wyrazu tablicy:",   tab.format)
tab.show()

# # zad 1.3 1.4
# def rysuj_ramke(w, h, grub): # grub grubość ramki w pikselach
#     t = (h, w)  # rozmiar tablicy
#     tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
#     for j in range(int(min(w,h)/grub)):
#         tab[j*grub:h - j*grub, j*grub:w - j*grub] = j % 2 # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
#     tab1 = tab.astype(np.bool_)
#     return tab1
#
# tab = rysuj_ramke(60, 120, 6)
# tab2 = Image.fromarray(tab)
# tab2.show()