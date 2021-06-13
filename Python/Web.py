import webbrowser
import random

site = input("Which site do you wanna open:\n1) Search for Something\n2) YouTube\n3) GitHub\n3) Stack Overflow\n4) Instagram\n5) FaceBook\n6) Twitter\n7) Random\n8) Something else (Site URL need to be provided later)\n")

if site == "1":
    engine = input("From which engine would you like to seach with\n1) Google\n2) Yahoo\n3) DuckDuckGo\n4) Bing\n5) Yandex\n6) WikiPedia\n")

    if engine == "1":      
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Search for image\n3) Just open it and search manually\n')
        
        if choice == "1":
            search = input('What do you wanna search for: ')
            webbrowser.open(f"http://www.google.com/search?q={search}")

        elif choice == "2":
            search = input('What do you wanna search the image for: ')
            webbrowser.open(f"http://www.google.com/search?q={search}&tbm=isch")

        elif choice == "3":
            webbrowser.open("www.google.com", new=1)
        
        else:
            print('Please give a valid input!')

    elif engine == "2":
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Search for image\n3) Just open it and search manually\n')
        
        if choice == "1":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://in.search.yahoo.com/search?p={search}')
        
        elif choice == "2":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://images.search.yahoo.com/search/images?p={search}')

        elif choice == "3":
            webbrowser.open_new_tab('https://yahoo.com')

        else:
            print("Please give a valid input!")

    elif engine == "3":
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Search for image\n3) Just open it and search manually\n')
        
        if choice == "1":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://duckduckgo.com/?q={search}')
        
        elif choice == "2":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://duckduckgo.com/?q={search}&iax=images&ia=images')

        elif choice == "3":
            webbrowser.open_new_tab('https://duckduckgo.com')

        else:
            print("Please give a valid input!")

    elif engine == "4":
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Search for image\n3) Just open it and search manually\n')
        
        if choice == "1":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://bing.com/?q={search}')
        
        elif choice == "2":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://www.bing.com/images/search?q={search}')

        elif choice == "3":
            webbrowser.open_new_tab('https://bing.com')

        else:
            print("Please give a valid input!")

    elif engine == "5":
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Search for image\n3) Just open it and search manually\n')
        
        if choice == "1":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://yandex.com/?q={search}')
        
        elif choice == "2":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://yandex.com/images/search?from=tabbar&text={search}')

        elif choice == "3":
            webbrowser.open_new_tab('https://yandex.com')

        else:
            print("Please give a valid input!")

    elif engine == "6":
        choice = input('\nPlease select one\n1) Search for some keyword\n2) Just open it and search manually\n')
        
        if choice == "1":
            search = input("What do you wanna search for: ")
            webbrowser.open(f'https://en.wikipedia.org/wiki/{search}')
        
        elif choice == "2":
            webbrowser.open(f'https://www.wikipedia.org')

        else:
            print("Please give a valid input!")

    else:
        print("Please giave a valid input!")

elif site == "2":
    webbrowser.open("www.youtube.com", new=1)

elif site == "3":
    webbrowser.open("www.github.com", new=1)

elif site == "4":
    webbrowser.open("www.stackoverflow.com", new=1)

elif site == "5":
    webbrowser.open("www.instagram.com", new=1)

elif site == "6":
    webbrowser.open("www.facebook.com", new=1)

elif site == "7":
    choice = input("\nRandom amoung which websites do you want to open:\n1) Any website\n2) Specific websites\n")
    if choice == "1":
        print("Sorry currently I cant do that please try out our other mathods!")
    
    elif choice == "2":
        websites = []
        sites = str(input("\nPlease give the URL of the websites amoung which you want to open a random one => "))
        websites.append(sites)
        while True:
            more = input("Add more (Y/N) => ").capitalize()

            if more == "Y":
                sites = str(input("\nPlease give the URL of the websites amoung which you want to open a random one => "))
                websites.append(sites)

            elif more == "N":
                break

        random_choice = random.choice(websites)
        print(f"\nOpening {random_choice} ...\n")
        webbrowser.open(random_choice, new=1) 

elif site == "8":
    site = input("Please paste the URL here => ")
    print(f"Opening {site} ...")
    webbrowser.open(site, new=1)

else:
    print("Please write a valid index number.")