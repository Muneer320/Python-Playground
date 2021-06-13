import requests
import os

def text_to_handwriting(string,save_to="Handwritting.png", rgb=[0,0,138]):
    data = requests.get("https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s"%(string,rgb[0],rgb[1],rgb[2])).content
    file = open(save_to,"wb")
    file.write(data)
    file.close()
    os.startfile(save_to)


text = input("Your text here >>> ")
text_to_handwriting(text, save_to="Beautiful sister.png")