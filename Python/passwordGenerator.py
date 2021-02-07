import string
import random
import os

print("\nA Completly random password generator\n\n")

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    while True:
        plen = int(input("Enter password Length: \n"))

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        pw = "".join(s[0:plen])

        print(pw + "\n\n")

        save = input("Shall i save the password in the 'password.txt'[Y/N]: ")
        save = save.lower()

        if save == "y":
            if(not os.path.exists("password.txt")):
                with open("password.txt", "w") as f:
                    f.write(f"Password: {pw}")
                    print("Password saved\n")
            else:
                with open("password.txt", "w") as f:
                    f.write(f"Password: {pw}")
                    print("Password saved\n")

        elif save == "n":
            pass

        else:
            print("Please write a valid character.")