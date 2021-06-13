import requests
import shutil

image_url = input("Please enter the image url here (Image URL would contain extensions also. Ex. .jpg, .png etc): ")
filename = image_url.split("/")[-1]

r = requests.get(image_url, stream = True)

if r.status_code == 200:
    r.raw.decode_content = True
    
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')