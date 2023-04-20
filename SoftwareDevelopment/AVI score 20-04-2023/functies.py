EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.


def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)


def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1


def getNumberOfCharacters(text: str) -> int:
    VarToReturn = len(text)
    return VarToReturn

# opdracht 2


def getNumberOfSentences(text: str) -> int:
    textstrvar = text
    amount_of_sentences_dots = textstrvar.count('.')
    amount_of_sentences_uitroeptekens = textstrvar.count('!')
    amount_of_sentences_questionmarks = textstrvar.count('?')
    total_sentences = (amount_of_sentences_dots + amount_of_sentences_uitroeptekens + amount_of_sentences_questionmarks)
    if total_sentences == 0:
        total_sentences = 1
   # print(total_sentences)
    return total_sentences

# opdracht 3


def getNumberOfWords(text: str) -> int:
    return len(text.split())


def getAviScore(text: str) -> int:
    funreturnvalue = getNumberOfWords(text)
    if funreturnvalue <= 7:
        return 5
    elif funreturnvalue == 8:
        return 6
    elif funreturnvalue == 9:
        return 7
    elif funreturnvalue == 10:
        return 8
    elif funreturnvalue == 11:
        return 11
    elif funreturnvalue > 11:
        return 12
