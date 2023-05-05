from string import ascii_letters, digits, punctuation
import random


def spam():
    chars = str(ascii_letters) + str(digits) + str(punctuation)
    spam = []

    while chars != '':
        for x in range(random.randint(10, 1000)):
            spam.append(chars[0])
        chars = chars[1:]

    random.shuffle(spam)

    spam = ''.join(spam)
    return spam


def countSpam(spam):
    chars = str(ascii_letters) + str(digits) + str(punctuation)
    count = {}

    for x in chars:
        count.update({chars[0]: 0})
        chars = chars[1:]

    while spam != '':
        count[spam[0]] += 1
        spam = spam[1:]

    return count


def main():
    s = spam()
    print(s, end="\n\n")
    counter = countSpam(s)
    print(counter)


if __name__ == "__main__":
    main()
