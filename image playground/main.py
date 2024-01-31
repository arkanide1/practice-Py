from PIL import Image, ImageFilter

img = Image.open("./images/pikachu.jpg")

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))


# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur.png' , 'png')

filtered_img = img.convert('L').rotate(180).filter(ImageFilter.SHARPEN)
box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
resize = cropped.resize((3000, 3000)).crop()

# filtered_img.show()

resize.save('grey.png', 'png')

img2 = Image.open("./astro.jpg")

img2.thumbnail((400, 400))

img2.save("good.png", "png")
