#we have a text file and we want to translate the content from it to a different language


#import the library
from translate import Translator
translator = Translator(to_lang='ja')
translator2 = Translator(to_lang='en')



#translate python library
#english to japanese
#read the file
try:
    with open('./text1.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./text1_japanese.txt',mode='w',encoding="utf-8") as my_file1:
            my_file1.write(translation)
except FileNotFoundError as e:
    print('check your file path')

#this saves the transalated file into the folder


#### japenese to english 
# check this again
#read the file
# try:
#     with open('./jap_response.txt', mode='r',encoding="utf-8") as my_file3:
#         text2 = my_file3.read()
#         translation2 = translator2.translate(text2)
#         with open('./eng_response.txt',mode='w',encoding="utf-8") as my_file2:
#             my_file2.write(translation2)
# except FileNotFoundError as e:
#     print('check your file path')



    
