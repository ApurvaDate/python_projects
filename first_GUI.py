#First GUI
#simulate when we have a graphical user interface
#How a computer will work just based on the learnt methods

#Exercise

picture =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#loop through the above list & display an empty space if we see 0 if 1 show *

#take this picture using space and * and display the image

#1 iterate over picture
    # if 0 -> print ''
    #if 1 -> print *
#we have to use end option in print

for row in picture:
    for pixel in row:

        if(pixel == 1):
            print('*',end='')
        else:
            print(' ',end='')
    print('')

#we also have to have an end line and 
#we add print('') after looping which will default to a new line

#we get Xmas tree here.


