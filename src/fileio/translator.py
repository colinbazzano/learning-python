from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open("src/fileio/translate.txt", 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("Check your file path brother")

"""translate not working


for some reason (unknown to me currently), the translate module is unable to be imported

I have tried:
pipenv installing it
pipenv shell to then see if it would work then
from both the Python and bash term's, tried to install the package directly.

probably is something easy on my end that I'm messing up but anyways, that's where I'm at with it.

"""
