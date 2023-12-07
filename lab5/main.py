from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

diff1 = Image.open('diff.png')

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)
    print("count ", s.count)
    print("mean ", s.mean)
    print("median ", s.median)
    print("stddev ", s.stddev)

statystyki(diff1)

hist = diff1.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2*256 + p])

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")

rysuj_histogram_RGB(diff1)


def zlicz_roznice_srednia_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent


print("Pierwsza roznica: ",zlicz_roznice_srednia_RGB(diff1, 5))
print("Druga roznica: ",zlicz_roznice_srednia_RGB(diff1, 25))
print("Trzecia roznica: ",zlicz_roznice_srednia_RGB(diff1, 50))


def zlicz_roznice_suma_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:  # poniżej równoważne sformułowania tego warunku
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent

print("Pierwsza suma: ", zlicz_roznice_suma_RGB(diff1, 5))
print("Druga suma: ", zlicz_roznice_srednia_RGB(diff1, 25))
print("Trzecia suma: ", zlicz_roznice_srednia_RGB(diff1, 50))

obraz1 = Image.open("obraz.jpg")
obraz1.save("obraz1.jpg")
obraz2 = Image.open("obraz1.jpg")
obraz2.save("obraz2.jpg")
obraz3 = Image.open("obraz2.jpg")
obraz3.save("obraz3.jpg")
obraz4 = Image.open("obraz3.jpg")
obraz4.save("obraz4.jpg")
obraz5 = Image.open("obraz4.jpg")
obraz5.save("obraz5.jpg")


def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0,2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)


def odkoduj(obraz1, obraz2):
    t_obraz1 = np.asarray(obraz1)
    t_obraz2 = np.asarray(obraz2)
    h, w, d = t_obraz1.shape
    result = np.zeros((h, w, d), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            if np.array_equal(t_obraz1[i, j, :], t_obraz2[i, j, :]):
                result[i, j, :] = 255  # biały piksel dla identycznych wartości
            else:
                result[i, j, :] = 0  # czarny piksel dla różnych wartości
    return Image.fromarray(result)


# Przykład użycia
obraz1 = Image.open("jesien.jpg")
obraz2 = Image.open("zakodowany2.bmp")
kod1 = odkoduj(obraz1, obraz2)
kod1.save("kod2.bmp")
