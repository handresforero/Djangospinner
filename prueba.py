# # # # ### Get sinonims of word reference
# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # url='http://www.wordreference.com/sinonimos/'
# # # # #enlace=input("palabra a buscar: ")
# # # # enlace= "nene"
# # # # buscar=url+enlace
# # # # resp=requests.get(buscar)
# # # # bs=BeautifulSoup(resp.text,'html')
# # # # lista=bs.find_all(class_='trans clickable')
# # # # for sin in lista:
# # # #     sino=sin.find_all('li')
# # # #     for fin in sino:
# # # #         print(fin.next_element)
# # # # print(sino)




# # import PyMultiDictionary
# # from PyMultiDictionary import MultiDictionary
# # # dictionary = MultiDictionary()
# # # print(dictionary.synonym('es', 'cantar'))

# # import nltk
# # #nltk.download('wordnet')

# # from nltk.corpus import wordnet
# # from nltk.tokenize import regexp_tokenize
# # import nltk.data
# # from nltk.stem.porter import *
# # import random

# # #an example of how to build a simple text spinner using nltk wordnet corpus
# # #obviusly you can modify this to work with any other synonym database

# # class spinner( object ):

# # #   function to spin spintax text using regex  
# # #   s = "{Spinning|Re-writing|Rotating|Content spinning|Rewriting} is {fun|enjoyable|entertaining|exciting|enjoyment}! try it {for yourself|on your own|yourself|by yourself|for you} and {see how|observe how|observe} it {works|functions|operates|performs|is effective}."
# # #   print spin(s)

# #   def spin(self, s):
# #     while True:
# #       s, n = re.subn('{([^{}]*)}',
# #             lambda m: random.choice(m.group(1).split("|")),
# #             s)

# #       if n == 0: break
# #     return s.strip()  

# # #  split a paragraph into sentences.
# # #  you can use the following replace and split functions or the nltk sentence tokenizer
# # #  content = content.replace("\n", ". ")
# # #  return content.split(". ")

# #   def splitToSentences(self, content):
# #     # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# #     tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
# #     return tokenizer.tokenize(content)  

# # #   get all synonyms of a word from the wordnet database

# #   def getSynonyms(self, word):
# # #     include the original word
# #     synonyms = [word]
# #     for syn in wordnet.synsets(word):
# #       for lemma in syn.lemmas():
# #         if lemma.name != word:
# # #           since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
# #           w, n = re.subn("_", " ", lemma.name())
# #           synonyms.append(w)
# #     s = list(set(synonyms))
# #     return len(s), s
  
# # #   transform text into spintax with the folowing steps
# # #   1. split the text to sentences
# # #   2. loop through the sentences and tokenize it
# # #   3. loop thorugh each token, find its stem and assemble all the synonyms of it into the spintax

# #   def getSpintax(self, text):
# #     sentences = self.splitToSentences(text)
# #     stemmer = PorterStemmer()
# #     spintax = ""
# #     for sentence in sentences:
# #       tokens = regexp_tokenize(sentence, "[\w']+")
# #       for token in tokens:
# #         stem = token
# #         n, syn = self.getSynonyms(stem)
# #         spintax += "{"
# #         spintax += token
# #         spintax += "|"

# #         for x in range(n):
# #           spintax += syn[x]
# #           if x < n-1:
# #             spintax += "|"
# #           else:
# #             spintax += "} "
# #     return spintax
# # #---------------------------------end of spinner class ---------------------------------#
# # if __name__ == '__main__':
# # # Assign the object for the class
# #     s = spinner()
# #     #st = "¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
# #     st = "¿Hola, cómo estás?, El día de hoy quiero cantar"
# #     spintax = s.getSpintax(st)
# #     print("spintax: ",spintax)
# #     spun = s.spin(spintax)
# #     print("spun: ",spun)

# def getSynonyms(self, word):
# #     include the original word
#     synonyms = [word]
#     for syn in wordnet.synsets(word):
#       for lemma in syn.lemmas():
#         if lemma.name != word:
# #           since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
#           w, n = re.subn("_", " ", lemma.name())
#           synonyms.append(w)
#     s = list(set(synonyms))
#     return len(s), s


import nltk 
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize 

cntxt1 = lesk(word_tokenize("El casco antiguo de Barcelona es muy bonito"), 
              "casco", synsets=wordnet.synsets("casco", lang="spa"))
print(cntxt1)