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
    print("Histogram norm:")
    print(normalized_hist)

    cumulated_hist = histogram_cumul(obraz_l)
    print("\nHistogram cumul:")
    print(cumulated_hist)

    equalized_image = histogram_equalization(obraz_l)
    equalized_image.show()
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
    plt.title("Eq Image")
    plt.imshow(equalized_image, cmap='gray')

    equalized_hist = histogram_norm(equalized_image)
    plt.subplot(2, 3, 5)
    plt.title("Eq Histogram")
    plt.plot(equalized_hist)

    plt.subplot(2, 3, 6)
    plt.title("Eq Cumul Histogram")
    equalized_cumul_hist = histogram_cumul(equalized_image)
    plt.plot(equalized_cumul_hist)

    plt.savefig("fig1.png")
    plt.show()

    statystyki(obraz_l)
    statystyki(equalized_image)

    # 3
    equalized_image_op = ImageOps.equalize(obraz_l)
    equalized_image_op.save("equalized1.png")

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(obraz_l, cmap='gray')

    plt.subplot(1, 3, 2)
    plt.title("Equalized Image (Custom)")
    plt.imshow(equalized_image, cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title("Equalized Image (ImageOps)")
    plt.imshow(equalized_image_op, cmap='gray')

    plt.savefig("fig2.png")
    plt.show()


    #  4
    def konwertuj1(obraz, w_r, w_g, w_b):
        img_array = np.array(obraz)
        l_channel = np.round(img_array[:, :, 0] * w_r + img_array[:, :, 1] * w_g + img_array[:, :, 2] * w_b).astype(
            np.uint8)
        return Image.fromarray(l_channel)


    mgla_image = Image.open("mgla.jpg")
    converted_image1 = konwertuj1(mgla_image, 0.299, 0.587, 0.114)
    converted_image1.save("mgla_L1.png")

    converted_image = mgla_image.convert('L')
    converted_image.save("mgla_L.png")

    statystyki(converted_image)
    statystyki(converted_image1)

    def konwertuj2(obraz, w_r, w_g, w_b):
        img_array = np.array(obraz)
        l_channel = (img_array[:, :, 0] * w_r + img_array[:, :, 1] * w_g + img_array[:, :, 2] * w_b).astype(int)
        return Image.fromarray(l_channel)


    converted_image2 = konwertuj2(mgla_image, 0.299, 0.587, 0.114)
    converted_image2.save("mgla_L2.png")

    statystyki(converted_image2)