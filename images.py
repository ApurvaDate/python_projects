from PIL import Image, ImageFilter


img = Image.open("pokedex/pikachu.png")

print(img)  #we get an object here
print(img.format) #PNG
print(img.size) #678,600

print(img.mode) #RGBA

print(dir(img))#here we get all the methods, we can also get this information in the documentation

#we can filter the image using ImageFilter from PIL
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img.save('pokedex/Blur_pikachu.png','png')

# filter_img = img.filter(ImageFilter.SMOOTH)
# filter_img.save('pokedex/smooth_pikachu.png','png') #JPEG might give and error but PNG supports all filters.

#we can use convert to convert image into different formats
filter_img = img.convert('L')
filter_img.save('pokedex/grey_pikachu.png','png')