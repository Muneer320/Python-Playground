text = input("Text >>> ")

res = ' '.join(format(ord(i), '08b') for i in text)
# res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))
  
print(f"The text after binary conversion : {res}")

copy = input('Copy to clipboard (Y/N): ').capitalize()
if 'Y' in copy:
    import pyperclip
    pyperclip.copy(res)
    print("Binary copied to clipboard.")