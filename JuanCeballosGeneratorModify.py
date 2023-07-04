"""
Program: JuanCeballosEmpWagesPd.py
Author: Juan P. Ceballos
Sentence generator
1. The input is
        Number of sentences
2. Computations
        Use the vocabualry from a set of text files at startup.
        Define a new single functions called "getWords."
        Function should expect file name as argument.
        Fuction should open an input file with the file's name.
        Defiena temporarelu list, read words from file, and add them to list.
        Function shiuls convert the list to "tuple" and retyrnt this "tuple".
        Call the funstions with and actual file nameto intialize each of the four vafiables for the vocabualry.
        Difine four simple funstions, one to create sentences, , another to create a nun phrase, the other one for a verb phrase, and the last one for crreatinga prepositional phrase.
3. Outputs:
        An actual file name will be created by the program to output the sentences.
"""
"""# Take the inputs, read the information and stored in the varibales verb, noun, preposition, article
verbs = open(verbs.txt, 'r')
verb = verbs.readlines()

nouns = open(nouns.txt, 'r')
noun = nouns.readlines()

articles = open(articles.txt, 'r')
article = article.readlines()

prepositions = open(prepositions.txt, 'r')
preposition = prepositions.readlines()"""


inputFile = open(verbs.txt, nouns.txt, articles.txt, prepositions.txt, 'r')

# Split the files verbs, nouns, prepositions, and articules into words, put them in a lists.
def getWords(inputFile):
    temporaryList = []
    inputFile.readlines()
    for line in inputFile:
        words = line.split()
        for word in words:
            temporaryList.append(word)
    tuple(temporaryList)
    return temporaryList
print(getWords)



"""wordNouns = []
for line2 in noun:
    wordN = line2.split()
    for wordNoun in wordN:
        wordNouns.append(wordNoun)

wordPrepositions = []
for line3 in preposition:
    wordP = line3.split()
    for wordPrepositon in wordP:
        wordPrepositons.append(wordPrepositon)

wordArticles = []
for line4 in article:
    wordA = line4.split()
    for wordArticle in wordA:
        wordArticles.append(wordArticle)"""

