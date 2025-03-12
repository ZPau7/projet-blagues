import pyjokes

def tell_joke():
    print(pyjokes.get_joke(language=lang))
    print("Hello")

if __name__ =="__main__":
    lang = input("Choisissez une langue (en, de, es, it, gl): ")
    joke_type = input("Choisissez une catégorie de blague (neutral,chuck,all):")
    tell_joke(lang, joke_type)
