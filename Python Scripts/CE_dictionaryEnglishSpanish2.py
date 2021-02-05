# Create a function that takes in a list of tuples (eng, spa), an English-Spanish dictionary, or (eng, fre), an English-French dictionary, depending on which languages you want your translator to work in. The function should return the dictionary you built.
def engSpan(engSpanList):
    engSpanDict=dict(engSpanList)
    return engSpanDict
engSpan([(I,yo),(want, quiero)])


# What happens if you try to translate your phrases from Spanish/French to English ?

# To test your dictionary, print out the translated phrases in both Spanish and French :
# I want sleep
# I want coffee
# Sleep is good
# Coffee is good

# Hint : You may want to call your function twice, once with each (eng, spa) and (eng, fre) to create two dictionaries.

# Add to your dictionary :
# English - Spanish
# I       -> Yo
# want    -> quiero
# one     -> un
# coffee  -> cafe
# tea     -> te
# is      -> es
# sleep   -> dormir
# eat     -> comer
# good    -> bueno

# English - French
# I       -> Je
# want    -> veux
# one     -> un
# is      -> est
# coffee  -> café (don't worry about the accent, cafe is fine)
# tea     -> thé  (don't worry about the accent, the is fine)
# sleep   -> dormir
# eat     -> manger
# good    -> bon


# List of tuples containing English - Spanish
engSpa = [("I", "Yo"), ("want", "quiero"), ("one", "un"), ("coffee", "cafe"), ("tea", "te"), ("is", "es"), ("sleep", "dormir"), ("eat", "comer"), ("good", "bueno")]

# List of tuples containing English - French
engFre = [("I", "Je"), ("want", "veux"), ("one", "un"), ("coffee", "cafe"), ("tea", "the"), ("is", "est"), ("sleep", "dormir"), ("eat", "manger"), ("good", "bon")]

# List of tuples containing Spanish - English
spaEng = [("Yo", "I"), ("quiero", "want"), ("un", "one"), ("cafe", "coffee"), ("te", "tea"), ("es", "is"), ("dormir", "sleep"), ("comer", "eat"), ("bueno", "good")]

# List of tuples containing French - English
freEng = [("Je", "I"), ("veux", "want"), ("un", "one"), ("cafe", "coffee"), ("the", "tea"), ("est", "is"), ("dormir", "sleep"), ("manger", "eat"), ("bon", "good")]



#-------------------------------------------

# Extra credit (10 points each):
# Code a function, called universalDict, that creates and returns a dictionary that works with multiple languages, i.e English-Spanish, Spanish-English, English-French, French-English (note this should be a single dictionary where I can pass in the original language, target language and a phrase and returns the translation as a string).
# Don't worry about handling translation for words that aren't in the dictionary.


# Build a dictionary dynamically. Make a function, called buildDict, that takes no parameters and prompts the user to enter the original language, the target language and then asks the user to enter a word in the original language and then prompts the user to enter the translation of that word in the target language.
# The function should prompt the user to enter as many words as he/she would like until the user wants to stop (you need to add a condition, i.e. the user enters nothing or the empty string, think of assignment 4 and picking a valid bin number).


# Create a function that takes in a dictionary, original language and target language, called gTranslate, and prompts the user to enter a phrase they want translated. Should handle words that are not in the dictionary, i.e. it should stay in the original language.
# For example : "I want sleep" --> returns "Yo quiero sleep" (here we assume the word sleep isn't in the dictionary). After printing out to console the translated phrase it should prompt the user to enter another phrase for translation until the user wants to stop.

#-------------------------------------------
