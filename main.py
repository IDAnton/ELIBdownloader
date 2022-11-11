import urllib.request
import os
import shutil
from PIL import Image


images = []
N = 5  # pages number
link = 'https://e-lib.nsu.ru/reader/service/SecureViewer/Page/UmVzb3VyY2UtMTAwNg/cGFnZTAwMDAw/'
dir_name = link[-13:-1]
os.mkdir(dir_name)
for i in range(0, N):
    urllib.request.urlretrieve(
        f'{link}{i}',
        f"{dir_name}/{i}.png")
    images.append(Image.open(f"{dir_name}/{i}.png"))
images[0].save(
    "out.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
shutil.rmtree(dir_name)
