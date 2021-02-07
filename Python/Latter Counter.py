while True:
    sentance = str(input("Write your sentance here:\n"))
    word = str(input("The number of which letter do you want to find out?\n"))

    sentance = sentance.lower()
    word = word.lower()

    words = 0

    for ltr in sentance:
        if ltr == word:
            words += 1

    print(f"The number of '{word}' in the sentance is {words}.")