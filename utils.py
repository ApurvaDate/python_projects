import settings

def height_prct(percentage):
    return ( settings.HEIGHT / 100 ) * percentage
#to get the % height from the original window height from settings.py
# we will use this in the original file
# print(height_prct(25))

#similar function will be defined for width

def width_prct(percentage):
    return (settings.WIDTH / 100) * percentage

