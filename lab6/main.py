from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('obraz.jpg')
inicjaly = Image.open('inicjaly.bmp')

def wstaw_inicjaly(obraz, inicjaly, kolor):
    obraz1 = obraz.copy()
    m = obraz.width - inicjaly.width
    n = obraz.height - inicjaly.height

    for y in range(inicjaly.height):
        for x in range(inicjaly.width):
            pixel = inicjaly.getpixel((x, y))
            if pixel != 255:
                obraz1.putpixel((m + x, n + y), kolor)

    return obraz1

def wstaw_inicjaly_maska(obraz, inicjaly, m, n,x,y, z):
    obraz2 = obraz.copy()
    for y in range(inicjaly.height):
        for x in range(inicjaly.width):
            pixel = inicjaly.getpixel((x, y))
            if pixel != 255:
                current_pixel = obraz2.getpixel((m + x, n + y))
                new_pixel = tuple(c + value for c, value in zip(current_pixel, (x, y, z)))
                obraz2.putpixel((m + x, n + y), new_pixel)
    return obraz2


obraz1 = wstaw_inicjaly(obraz,inicjaly, (255, 0, 0))
obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, (obraz.width - inicjaly.width) // 2, (obraz.height - inicjaly.height) // 2, 50, 50, 50)
obraz1.save("obraz1.jpg")
obraz2.save("obraz2.jpg")


def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    inicjaly_pixels = inicjaly.load()
    obraz1_pixels = obraz1.load()

    for y in range(inicjaly.height):
        for x in range(inicjaly.width):
            pixel = inicjaly_pixels[x, y]
            if pixel != 255:
                obraz1_pixels[m + x, n + y] = kolor

    return obraz1

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    obraz2 = obraz.copy()

    inicjaly_pixels = inicjaly.load()
    obraz2_pixels = obraz2.load()

    for y in range(inicjaly.height):
        for x in range(inicjaly.width):
            pixel = inicjaly_pixels[x, y]
            if pixel == 255:
                current_pixel = obraz2_pixels[m + x, n + y]
                new_pixel = tuple(c + value for c, value in zip(current_pixel, (x, y, z)))
                obraz2_pixels[m + x, n + y] = new_pixel

    return obraz2

obraz_z_inicjalami = wstaw_inicjaly_load(obraz, inicjaly, obraz.width - inicjaly.width, obraz.height - inicjaly.height, (255, 0, 0)).show()
obraz_z_maska = wstaw_inicjaly_maska_load(obraz, inicjaly, (obraz.width - inicjaly.width) // 2, (obraz.height - inicjaly.height) // 2, 50, 50, 50).show()



def kontrast(obraz, kontrast):
    obraz2 = obraz.copy()
    mn = ((255 + kontrast) / 255) ** 2
    return obraz2.point(lambda i: 128 + (i - 128) * mn)

kontrast1 = kontrast(obraz, 50)
kontrast2 = kontrast(obraz, 100)
kontrast3 = kontrast(obraz, 150)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(obraz)
axes[0, 0].set_title('Oryginalny')
axes[0, 1].imshow(kontrast1)
axes[0, 1].set_title('Kontrast 50')
axes[1, 0].imshow(kontrast2)
axes[1, 0].set_title('Kontrast 100')
axes[1, 1].imshow(kontrast3)
axes[1, 1].set_title('Kontrast 150')
plt.savefig("fig1.png")


def transformacja_logarytmiczna(obraz):
    obraz2 = obraz.copy()
    return obraz2.point(lambda i: int(255 * np.log(1 + i / 255)))


def filtr_liniowy(obraz, a, b):
    obraz2 = obraz.copy()
    return obraz2.point(lambda i: int(max(0, min(255, a * i + b))))


obraz_log = transformacja_logarytmiczna(obraz)
obraz_filtr = filtr_liniowy(obraz, 2, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(obraz)
axes[0].set_title('Oryginalny')

axes[1].imshow(obraz_log)
axes[1].set_title('Transformacja logarytmiczna')

axes[2].imshow(obraz_filtr)
axes[2].set_title('Filtr liniowy (a=2, b=100)')
plt.savefig("fig2.png")


def transformacja_gamma(obraz, gamma):
    obraz2 = obraz.copy()
    return obraz2.point(lambda i: int((i / 255) ** (1 / gamma) * 255))


gamma1 = transformacja_gamma(obraz, 0.5)
gamma2 = transformacja_gamma(obraz, 1.0)
gamma3 = transformacja_gamma(obraz, 1.5)


fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(np.array(obraz))
axes[0].set_title('Orginalny obraz')
axes[1].imshow(np.array(gamma1))
axes[1].set_title('Gamma 0.5')
axes[2].imshow(np.array(gamma2))
axes[2].set_title('gamma 1.0')
axes[3].imshow(np.array(gamma3))
axes[3].set_title('gamma 1.5')

plt.savefig("fig3.png")
plt.show()
