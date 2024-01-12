# Change png image to ico img
from PIL import Image

def png_to_ico(png_path, ico_path):
    img = Image.open(png_path)
    img.save(ico_path, format='ICO')

# Sử dụng hàm
png_to_ico('D:\\Downloads\\Genshin Costumized Folder Icon\\Character Gacha Art Folders\\ayaka0.png', 'D:\\Downloads\\Genshin Costumized Folder Icon\\Character Gacha Art Folders\\ayaka0.ico')