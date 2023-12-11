from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # dla wersji 3.5.2
from PIL import ImageOps
from PIL import ImageStat as stat


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

# 2.1
def histogram_norm(obraz):
    img_array = np.array(obraz)
    hist, bins = np.histogram(img_array.flatten(), bins=256, range=[0, 256])
    norm_hist = hist / float(img_array.size)
    return norm_hist

# 2.2
def histogram_cumul(obraz):
    img_array = np.array(obraz)
    hist, bins = np.histogram(img_array.flatten(), bins=256, range=[0, 256])
    cumul_hist = np.cumsum(hist)
    return cumul_hist

# 2.3
def histogram_equalization(obraz):
    img_array = np.array(obraz)
    cumul_hist = histogram_cumul(obraz)
    cumul_hist_normalized = (cumul_hist / float(img_array.size)) * 255
    equalized_image = np.interp(img_array.flatten(), range(256), cumul_hist_normalized).reshape(img_array.shape)
    equalized_image = equalized_image.astype(np.uint8)
    return Image.fromarray(equalized_image)


    # 2.4
if __name__ == "__main__":
    im = Image.open("zeby.png")
    obraz_l = im.convert("L")
    normalized_hist = histogram_norm(obraz_l)
    cumulated_hist = histogram_cumul(obraz_l)

    equalized_image = histogram_equalization(obraz_l)
    equalized_image.save("equalized.png")

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 3, 1)
    plt.title("Original Image")
    plt.imshow(obraz_l, cmap='gray')

    plt.subplot(2, 3, 2)
    plt.title("Norm Histogram")
    plt.plot(normalized_hist)

    plt.subplot(2, 3, 3)
    plt.title("Cumul Histogram")
    plt.plot(cumulated_hist)

    plt.subplot(2, 3, 4)
    plt.title("Equalized Image")
    plt.imshow(equalized_image, cmap='gray')

    equalized_hist = histogram_norm(equalized_image)
    plt.subplot(2, 3, 5)
    plt.title("Equalized Histogram")
    plt.plot(equalized_hist)

    plt.subplot(2, 3, 6)
    plt.title("Equalized Cumul Histogram")
    equalized_cumul_hist = histogram_cumul(equalized_image)
    plt.plot(equalized_cumul_hist)

    plt.savefig("fig1.png")


    print("Obraz L:")
    statystyki(obraz_l)
    print("\nEqualized image:")
    statystyki(equalized_image)

    # 3
    equalized_image_ops = ImageOps.equalize(obraz_l)
    equalized_image_ops.save("equalized1.png")

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Orginalny obraz L")
    plt.imshow(obraz_l, cmap='gray')

    plt.subplot(1, 3, 2)
    plt.title("Equalized Image")
    plt.imshow(equalized_image, cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title("Equalized Image (ImageOps)")
    plt.imshow(equalized_image_ops, cmap='gray')

    plt.savefig("fig2.png")
    # plt.show()


    #  4
    def konwertuj1(obraz, w_r, w_g, w_b):
        if abs(w_r + w_g + w_b - 1) > 0.001:  # Porównanie z małą wartością bezwzględną
            raise ValueError("Suma wag w_r, w_g, w_b musi być równa 1")

        img = obraz.convert('RGB')
        img_l = Image.new('L', img.size)

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                l = int(round(r * w_r + g * w_g + b * w_b))
                img_l.putpixel((x, y), l)

        return img_l

    def konwertuj2(obraz, w_r, w_g, w_b):
        if abs(w_r + w_g + w_b - 1) > 0.001:
            raise ValueError("Suma wag w_r, w_g, w_b musi być równa 1")
        img = obraz.convert('RGB')
        img_l = Image.new('L', img.size)

        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                l = int(r * w_r + g * w_g + b * w_b)
                img_l.putpixel((x, y), l)
        return img_l

    obraz = Image.open('mgla.jpg')

    mgla_L1 = konwertuj1(obraz, 0.299, 0.587, 0.114)
    mgla_L1.save('mgla_L1.png')

    mgla_L = obraz.convert('L')
    mgla_L.save('mgla_L.png')

    mgla_L2 = konwertuj2(obraz, 0.299, 0.587, 0.114)
    mgla_L2.save('mgla_L2.png')

    print("\nMgla L:")
    statystyki(mgla_L)
    print("\nMgla L1:")
    statystyki(mgla_L1)
    print("\nMgla L2")
    statystyki(mgla_L2)