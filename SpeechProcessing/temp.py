import os
from PIL import Image

def convert_png_to_ico_folder(folder_path, output_folder):
    # Duyệt qua tất cả các phần tử con trong thư mục
    for filename in os.listdir(folder_path):
        # Kiểm tra nếu là file PNG
        if filename.endswith('.png'):
            # Tạo đường dẫn đầy đủ đến file PNG
            png_path = os.path.join(folder_path, filename)
            
            # Tạo đường dẫn đến file ICO
            ico_filename = os.path.splitext(filename)[0] + '.ico'
            ico_path = os.path.join(output_folder, ico_filename)
            
            # Chuyển đổi từ PNG sang ICO
            img = Image.open(png_path)
            img.save(ico_path, format='ICO')

# Sử dụng
convert_png_to_ico_folder('D:\\Downloads\\Genshin Costumized Folder Icon\\Namecard Art Folders', 'D:\\Downloads\\Genshin Costumized Folder Icon\\Namecard Art Folders')
