import pyshorteners

while True:
    try:
        url = input("Enter your url: ")
        s = pyshorteners.Shortener().tinyurl.short(url)
        print("Your shorted is -->", s)
    except Exception as e:
        print(e)