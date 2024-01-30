from translate import Translator

translator = Translator(to_lang='fr')
try:
    with open("source.txt", "r") as file:
        text = file.read()

        translation = translator.translate(text)

        #print(translation)
        with open("dest.txt", "w") as file:
            file.write(translation)


except FileNotFoundError as err:
    print("file doesn't exist")
except IOError as err:
    print("io error")
except Exception as err:
    print("Error during translation:", err)


# still dont know why i cant put the result off some
# languages {ar , ja ...} to another file but dtill works fine
