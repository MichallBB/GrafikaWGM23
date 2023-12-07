from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('obraz.jpg')

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    max = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            for i in range(3):
                if pixel[i] > max[i]:
                    max[i] = pixel[i]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = tuple(max)
    return obraz1


im1 = im.copy()
im1 = rysuj_kwadrat_max(im1, 299, 22, 55)
im1.save("obraz1.png")



def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    min = [255, 255,255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            for i in range(3):
                if pixel[i] < min[i]:
                    min[i] = pixel[i]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = tuple(min)

    return obraz1

im2 = im.copy()
im2 = rysuj_kwadrat_min(im2, 60, 170, 25)
im2.save("obraz2.png")


def skopiuj_kolo(obraz, m_s, n_s, r, m_kopia, n_kopia):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i in range(w):
        for j in range(h):
            if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:
                x = i + (m_kopia - m_s)
                y = j + (n_kopia - n_s)
                if 0 <= x < w and 0 <= y < h:
                    pixel = obraz.getpixel((x, y))
                    obraz1.putpixel((i, j), pixel)
    return obraz1

im_kolo = skopiuj_kolo(im, 80, 144, 17, 47, 172)
im_kolo.save("obraz3.png")

im4 = skopiuj_kolo(im, 80, 144, 17, 47, 172)
im5 = skopiuj_kolo(im4, 80, 100, 17, 47, 172)
im6 = skopiuj_kolo(im5, 45, 60, 17, 47, 172)
im7 = skopiuj_kolo(im6, 7, 144, 17, 47, 172)
im8 = skopiuj_kolo(im7, 7, 100, 17, 47, 172)
im8.save("obraz4.png")

def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img

obicie = odbij_w_pionie(im).show()
