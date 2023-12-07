from PIL import Image

# Wczytanie obrazu
obraz = Image.open('obraz11.jpg')

# Rozdzielenie kanałów
r, g, b = obraz.split()

# Tworzenie nowego obrazu mieszając kanały
mix_obraz = Image.merge('RGB', (b, g, r)).show()

# Zapisanie obrazu mix_obraz.save('mixobraz11.jpg')