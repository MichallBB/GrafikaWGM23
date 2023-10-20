from PIL import Image
import numpy as np
import random

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg

# kolor szarosci jest generowana przez random.randint
def rysuj_ramke(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for j in range(int(min(w,h)/grub)):
        tab[j*grub:h - j*grub, j*grub:w - j*grub] = random.randint(0,240)
    return tab

ramka = Image.fromarray(rysuj_ramke(480, 320, 10))
ramka.save("obraz1_1.jpg")
ramka.save("obraz1_1.png")
ramka2 = Image.fromarray(negatyw_szare(ramka))
ramka2.save("obraz1_1N.jpg")
ramka2.save("obraz1_1N.png")

def pionowe_paski(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile2 = int(w / grub)
    j = 0
    tab_pom = [10,20,30,50]
    for k in range(ile2):
        tab[:,j:j+grub] = random.randint(0,250)
        j = k * grub
    tab = tab * 255
    return Image.fromarray(tab)

pionowe = pionowe_paski(480, 320, 15)
pionowe.save("obraz1_2.jpg")
pionowe.save("obraz1_2.png")
pionowe_neg = Image.fromarray(negatyw_szare(pionowe))
pionowe_neg.save("obraz1_2N.jpg")
pionowe_neg.save("obraz1_2N.png")
