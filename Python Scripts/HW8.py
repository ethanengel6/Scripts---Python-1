# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MtEkwzrzkzPKWDWinU0mEeUyR6NMA5NM

1. Write a function, called checkPalindrome, that takes a string as an argument and determines if the string is a palindrome. (20 points)  A palindrome is a string that is the same forward and backward like: level or noon.
"""

def checkPalindrome(maybeDrome)
""""
Arg:maybeDrome(string)
No return, but takes the string & prints whether it is a palindrome or not"""

  forwardList=[]
  backwardList=[]
  for w in range(len(maybeDrome)):
    forwardList.append(maybeDrome[w])
    backwardList.append(maybeDrome[len(maybeDrome)-1-w])
  if forwardList==backwardList:
    print("The string is a palindrome!")
  else:
    print("No drome!")
checkPalindrome("gohangasalamiimalasagnahog")

"""2. Create a function, called sortStrings, that takes a list of strings and sorts the list based on the length of string from lower to higher. (20 points)"""

def sortStrings(stringList):
"""
Arg:stringList(list of strings)

returns:stringList(list of strings); rearranged from least to greatest length of characters"""
  for q in range(len(stringList),1,-1):
    for z in range(len(stringList),1,-1):
        if len(stringList[z-1])<len(stringList[z-2]):
            stringList.insert(z-2,stringList.pop(z-1))
  print(stringList)
sortStrings(["My","jumper","is","wet"])

"""3. Write a function, called mixedString, that takes a word string and computes a list of all words generated by a single swap of letters in the word. (20 points)  For example dog should return ['odg', 'god', ‘dgo'] (notice that letters are only swapped with their immediate neighbors only, i.e. you don’t have ‘ogd’)"""

def mixedString(wordString):
"""
Arg:wordString(string)
string to have 2 consecutive characters inverted in every way possible

returns: mixedWordList(list)
list of all of the new strings created by the inversion of characters as mentioned above
"""
  unmixedWordList=[]
  mixedWordList=[]
  tempString=""
  tempList=[]
  mixedString=""
  noSpace=""

  for gg in range(len(wordString)):
    unmixedWordList.append(wordString)


  for d in range(len(wordString)):
    tempString=unmixedWordList[d]
    tempList=list(tempString)
    tempList[d],tempList[d-1]=tempList[d-1],tempList[d]
    mixedString=noSpace.join(tempList)
    mixedWordList.append(mixedString)

  return(mixedWordList)
mixedString("Yourmamasallama")

"""4. Write a function, called reversePhrase, that takes a string of words and returns the string with the words in reverse order. You cannot use any library methods or functions.  (20 points)  For example if the sentence is: “I love python”, then the function returns: “python love I”"""

def reversePhrase(stringofWords):
"""
Arg:stringofWords(string) separated by spaces

returns: backwardString(string)
the same words from the argument string in reverse order
"""
  backwardList=[]
  forwardList=stringofWords.split(" ")
  finalFrontier=" "
  for qw in range(len(forwardList)):
      backwardList.append(forwardList[len(forwardList)-1-qw])
  backwardString=finalFrontier.join(backwardList)
  return(backwardString)
reversePhrase("I really don't know anymore")

"""5. Write a function, called uniqueLetters, that takes a string as an argument and returns a new string with no duplicated letters. (20 points)  For example if the word is: “application” then the function returns “aplicton”"""

def uniqueLetters(stringtoReduce):
"""
Arg:stringtoReduce(string); one word string

returns: reducedString(string)
the same word written with no characters appearing more than once"""

  chopBlockList=[]
  nothing=""
  listtoReduce=list(stringtoReduce)
  for bk in range(len(listtoReduce)):
    if listtoReduce.count(listtoReduce[bk])>1 and (listtoReduce.count(listtoReduce[bk])-chopBlockList.count(listtoReduce[bk])>1):
        chopBlockList.append(listtoReduce[bk])
  for getout in range(len(chopBlockList)):
    listtoReduce.remove(chopBlockList[getout])
  reducedString=nothing.join(listtoReduce)
  return (reducedString)
uniqueLetters("Pneumonoultramicroscopicsilicovolcanoconiosis")
