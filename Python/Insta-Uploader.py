from instabot import Bot

bot = Bot()


uName = input("Username >>> ")
password = input("Password >>> ")

bot.login(username = uName, password = password)

bot.upload_photo("avatar.png", caption="Auto Test Upload using Python (Ignore Please ;)")