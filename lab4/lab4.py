from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# Zadanie 2a

im1 = Image.open('obraz.jpg')
T = np.array(im1)

t_r = T[:, :, 0]
im_r = Image.fromarray(t_r)
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)

# Zadanie 2b

im2 = Image.merge('RGB', (im_r, im_g, im_b))
im1_im2_diff = ImageChops.difference(im1, im2)

# Zadanie 2c

plt.figure(figsize=(9, 4))

plt.subplot(1, 3, 1)
plt.imshow(im1)
plt.axis('off')
plt.title('Obraz wejściowy im1')

plt.subplot(1, 3, 2)
plt.imshow(im2)
plt.axis('off')
plt.title('Obraz po zamianie im2')

plt.subplot(1, 3, 3)
plt.imshow(im1_im2_diff)
plt.axis('off')
plt.title('Różnica im1_im2_diff')

plt.savefig('fig1.png')

# Zadanie 3a
r, g, b = im1.split()
im3 = Image.merge('RGB', (g, b, r))
im3.save('im3.jpg')
im3.save('im3.png')

# Zadanie 3b
im3_jpg = Image.open('im3.jpg')
im3_png = Image.open('im3.png')
diff = ImageChops.difference(im3_png, im3_jpg)

# Zadanie 3c
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(im3_jpg)
plt.axis('off')
plt.title('Obraz im3.jpg')

plt.subplot(1, 3, 2)
plt.imshow(im3_png)
plt.axis('off')
plt.title('Obraz im3.png')

plt.subplot(1, 3, 3)
plt.imshow(diff)
plt.axis('off')
plt.title('Różnica diff')

plt.savefig('fig2.png')

# Zadanie 4a
obraz1_1_jpg = Image.open('obraz1_1.jpg')
obraz1_1_png = Image.open('obraz1_1.png')
obraz1_1N_jpg = Image.open('obraz1_1N.jpg')
obraz1_1N_png = Image.open('obraz1_1N.png')
obraz1_2_jpg = Image.open('obraz1_2.jpg')
obraz1_2_png = Image.open('obraz1_2.png')
obraz1_2N_jpg = Image.open('obraz1_2N.jpg')
obraz1_2N_png = Image.open('obraz1_2N.png')

diff1 = ImageChops.difference(obraz1_1_jpg, obraz1_1_png)
diff2 = ImageChops.difference(obraz1_1N_jpg, obraz1_1N_png)
diff3 = ImageChops.difference(obraz1_2_jpg, obraz1_2_png)
diff4 = ImageChops.difference(obraz1_2N_jpg, obraz1_2N_png)

# Przedstawienie 4 obrazów z zadania 4 na jednej figurze plt
plt.figure(figsize=(12, 8))

plt.subplot(4, 3, 1)
plt.imshow(obraz1_1_jpg, 'gray')
plt.axis('off')

plt.subplot(4, 3, 2)
plt.imshow(obraz1_1_png, 'gray')
plt.axis('off')

plt.subplot(4, 3, 3)
plt.imshow(diff1, 'gray')
plt.title("diff")
plt.axis('off')

plt.subplot(4, 3, 4)
plt.imshow(obraz1_1N_jpg, 'gray')
plt.axis('off')

plt.subplot(4, 3, 5)
plt.imshow(obraz1_1N_png, 'gray')
plt.axis('off')

plt.subplot(4, 3, 6)
plt.imshow(diff2, 'gray')
plt.axis('off')

plt.subplot(4, 3, 7)
plt.imshow(obraz1_2_jpg, 'gray')
plt.axis('off')

plt.subplot(4, 3, 8)
plt.imshow(obraz1_2_png, 'gray')
plt.axis('off')

plt.subplot(4, 3, 9)
plt.imshow(diff3, 'gray')
plt.axis('off')

plt.subplot(4, 3, 10)
plt.imshow(obraz1_2N_jpg, 'gray')
plt.axis('off')

plt.subplot(4, 3, 11)
plt.imshow(obraz1_2N_png, 'gray')
plt.axis('off')

plt.subplot(4, 3, 12)
plt.imshow(diff4, 'gray')
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()


#Zad 5
im_input = Image.open('obraz.jpg')
width, height = im1.size
gray_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)
im4 = Image.fromarray(gray_array, mode='L')

im_r = Image.merge('RGB', (im4, im1.getchannel('G'), im1.getchannel('B')))
im_g = Image.merge('RGB', (im1.getchannel('R'), im4, im1.getchannel('B')))
im_b = Image.merge('RGB', (im1.getchannel('R'), im1.getchannel('G'), im4))

plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(im_input)
plt.axis('off')
plt.title('Obraz wejściowy')

plt.subplot(1, 4, 2)
plt.imshow(im_r)
plt.axis('off')
plt.title('Zamiana kanału R')

plt.subplot(1, 4, 3)
plt.imshow(im_g)
plt.axis('off')
plt.title('Zamiana kanału G')

plt.subplot(1, 4, 4)
plt.imshow(im_b)
plt.axis('off')
plt.title('Zamiana kanału B')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig4.png')
plt.show()


#Zad6
width, height = 200, 200
czarne_tlo = np.zeros((height, width), dtype=np.uint8)

bialy_ksztalt = np.ones((height // 2, width // 2), dtype=np.uint8) * 255
image1 = czarne_tlo.copy()
image1[50:50+bialy_ksztalt.shape[0], 50:50+bialy_ksztalt.shape[1]] = bialy_ksztalt
image2 = czarne_tlo.copy()
image2[50:50+bialy_ksztalt.shape[0], 100:100+bialy_ksztalt.shape[1]] = bialy_ksztalt
image3 = czarne_tlo.copy()
image3[100:100+bialy_ksztalt.shape[0], 75:75+bialy_ksztalt.shape[1]] = bialy_ksztalt

# Tworzenie obrazów RGB z kanałów
rgb_1 = np.stack([image1, image2, image3], axis=-1)
rgb_2 = np.stack([image1, image3, image2], axis=-1)
rgb_3 = np.stack([image2, image1, image3], axis=-1)
rgb_4 = np.stack([image2, image3, image1], axis=-1)
rgb_5 = np.stack([image3, image1, image2], axis=-1)
rgb_6 = np.stack([image3, image2, image1], axis=-1)

# Wyświetlenie i zapis obrazów
plt.figure(figsize=(12, 4))

plt.subplot(2, 3, 1)
plt.imshow(rgb_1, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 1')

plt.subplot(2, 3, 2)
plt.imshow(rgb_2, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 2')

plt.subplot(2, 3, 3)
plt.imshow(rgb_3, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 3')

plt.subplot(2, 3, 4)
plt.imshow(rgb_4, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 4')

plt.subplot(2, 3, 5)
plt.imshow(rgb_5, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 5')

plt.subplot(2, 3, 6)
plt.imshow(rgb_6, cmap='gray')
plt.axis('off')
plt.title('Obraz RGB 6')

plt.savefig('fig5.png')