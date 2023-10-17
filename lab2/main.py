from PIL import Image
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
        tab[j*grub:h - j*grub, j*grub:w - j*grub] = j % 2
    tab1 = tab.astype(np.bool_)
    return tab1

tab = rysuj_ramke(480, 320, 10)
tab22 = Image.fromarray(tab)
#tab22.show()
tab22.save("zad3.1.1.bmp")

# 3.1.2

def pionowe_paski(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile2 = int(w / grub)
    j = 0
    for k in range(ile2):
        tab[:,j:j+grub] = (k+1) % 2
        j = k * grub
    tab = tab * 255
    return Image.fromarray(tab)

tab77 = pionowe_paski(480, 320, 10)
print("typ danych tablicy", tab.size)
#print("rozmiar wyrazu tablicy:",   tab.format)
#tab77.show()
tab77.save("zad3.1.2.bmp")

# zad 1.3 1.4
def rysuj_obraz3(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[0:n, 0:m] = 0
    tab[n:h, m:w] = 0
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

tab5 = rysuj_obraz3(480, 320, 100,50)
tab5.show()
tab5.save("zad3.1.3.bmp")

# funkcja rysuje linie tak dluga jak podana jest wartosc argumentu len (w pikselach), linia jest tworzona od lewej do prawej
# w = szerokosc obrazu, h = wysokosc obrazu, grub = grubosc lini, len = dlugosc lini jaka ma byc
def rysuj_obraz4(w, h, grub, len):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    wysokosc_pocz = grub
    rzad = 0
    while(len > 0):
        if(len > w):
            # sprawdza czy rzad pierwszy poniewaz linia rozpoczyna sie od marginesu (od lewej strony)
            if rzad == 0:
                tab[wysokosc_pocz:wysokosc_pocz+grub, 5:] = 0
            else:
                tab[wysokosc_pocz:wysokosc_pocz + grub, :] = 0
            wysokosc_pocz = wysokosc_pocz + grub * 2
            len -= w
            rzad += 1
            continue
        rzad += 1
        if(int(h/grub) <= rzad*2):
            print("brak miejsca")
            break
        tab[wysokosc_pocz:wysokosc_pocz+grub,:len] = 0
        len = 0
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

tab6 = rysuj_obraz4(480, 320, 10,5000)
#tab6.show()
tab6.save("zad3.1.4.bmp")

def wstaw_obraz_w_obraz(obraz_bazowy,obraz_wstawiany, m, n):
    # w,h rozmiary nowego obrazu, m<=w,  n<=h (m,n miejsce wstawienia obrazu )
    tab_obraz = np.asarray(obraz_wstawiany)*1
    h0, w0 = tab_obraz.shape
    h = obraz_bazowy.height
    w = obraz_bazowy.width
    tab = np.asarray(obraz_bazowy)*1
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    print(n_k, m_k)
    print(n_p, m_p)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz[i - n][j - m]
    tab = tab.astype(bool) # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

obraz = wstaw_obraz_w_obraz(tab6,inicjaly ,300,90)
obraz.show()
obraz.save("wstaw1.bmp")
obraz2 = wstaw_obraz_w_obraz(tab6,inicjaly ,10,290)
obraz2.save("wstaw2.bmp")
