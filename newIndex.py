#IWU - CIS - 125

#Gabe Brown


sortLetters = ""
word = ""
import string

def sortLetter(word):
    word = word.lower()
    listWord = list(word)
    listWord.sort()
    sortedLetters = ''.join(listWord)
    
    return sortedLetters

def createDictionary(fileName, dictionary):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        word = line.lower()
        if word[0] == 'v':
            sortedWord = sortLetter(word)
            dictionary[sortedWord] == word
    fileHandle.close()    

def findAnagrams(fileName, dictionary):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        quizword = line.lower()
        print(quizword, dictionary[sortLetter(quizword)])
    fileHandle.close()  

def printAnagrams(fileName, dictionary):
    pass


def main():
    aDict = {}
    fileName = 'wordList.txt'
    quizListName = 'quizword.txt'
    createDictionary(fileName, aDict)
    findAnagrams(quizListName, aDict)