from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rysuj_ramke_kolor(w, h, dzielnik, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = 255, 0, 0
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor
    return tab

#Image.fromarray(rysuj_ramke_kolor(100, 60, 3, 100, 200, 300)).show()


def szary(w, h):
    tab = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (i - j) % 256
    return tab

# Wczytanie obrazu "mgla.jpg"
img_color = Image.open("mgla.jpg")

# Pobranie wymiarów obrazu
width, height = img_color.size

# Stworzenie trzech obrazów szarych o tych samych wymiarach co "mgla.jpg"
gray_r = szary(width, height)
gray_g = szary(width, height)
gray_b = szary(width, height)

# Zastąpienie odpowiednich kanałów R, G, B obrazu "mgla.jpg" obrazami szarymi
img_r = np.array(img_color)
img_r[:, :, 0] = gray_r

img_g = np.array(img_color)
img_g[:, :, 1] = gray_g

img_b = np.array(img_color)
img_b[:, :, 2] = gray_b

# Wyświetlenie obrazów na jednym wykresie
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

axes[0].imshow(img_color)
axes[0].set_title('Original')

axes[1].imshow(Image.fromarray(img_r))
axes[1].set_title('Red Channel Replaced')

axes[2].imshow(Image.fromarray(img_g))
axes[2].set_title('Green Channel Replaced')

axes[3].imshow(Image.fromarray(img_b))
axes[3].set_title('Blue Channel Replaced')

plt.tight_layout()

# Zapisanie wykresu jako obraz "mix.png"
plt.savefig('mix.png')
plt.show()