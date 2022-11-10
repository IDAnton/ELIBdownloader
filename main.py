import urllib.request
from PIL import Image


images = []
N = 195  # pages number
link = 'https://e-lib.nsu.ru/reader/service/SecureViewer/Page/UmVzb3VyY2UtMTAwNg/cGFnZTAwMDAw/'
for i in range(0, N):
    urllib.request.urlretrieve(
        f'{link}{i}',
        f"data/{i}.png")
    images.append(Image.open(f"data/{i}.png"))
images[0].save(
    "out.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)