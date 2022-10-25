from rembg import remove
from PIL import Image

# importa imagem original
img = Image.open('img.jpg')

#Remove fundo da imagem
img_without_back = remove(img)

# salva imagem sem fundo
img_without_back.save('image_without_back.png')