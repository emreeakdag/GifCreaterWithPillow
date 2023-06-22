from PIL import Image


# Fotoğrafların yolu için liste oluşturalım.
image_path_list = ['dog-1.jpg', 'dog-2.jpg', 'dog-3.jpg', 'dog-4.jpg']

# Resimler için bir liste oluşturalım
image_list = [Image.open(file) for file in image_path_list]
