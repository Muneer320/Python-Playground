import string
import random


alphabetList = [x for x in string.ascii_lowercase]

def getWord(num):
    word = []
    for x in range(num):
        for x in range(random.randint(3, 7)):
            word.append(alphabetList[random.randint(0, len(alphabetList)-1)])
        word.append(' ')
    return ''.join(word)

if __name__=="__main__":
    print(getWord(int(input("No. of words >>> "))))