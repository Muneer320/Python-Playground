from translate import Translator

while True:

    from_lang = input('From which language do you want to translate your text?\n')
    to_lang = input('In which language do you want your result in?\n')

    trans = input('What do you want to translate?\n')
    
    translator = Translator(from_lang = from_lang, to_lang = to_lang)
    result = translator.translate("\n\n" + trans)
    print(result)