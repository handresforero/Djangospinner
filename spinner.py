# #conda activate ppSpinner
# #cd D:\Woobsing\Spinner\ppSpinner

# #conda install -c anaconda nltk
# #pip install urllib3

# import nltk
# import random
# import urllib
# from urllib.request import urlopen

# u = "http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html"
# # used for reading data of xml format
# from bs4 import BeautifulSoup 
# #Reading the data
# positive_reviews = urlopen(u).read()
# positive_reviews = BeautifulSoup(positive_reviews)
# positive_reviews = positive_reviews.find_all('p')


# #print(positive_reviews[1:5])
# #print(positive_reviews)


# from builtins import range
# #Initialize an Empty Dictionary
# trigrams = {}

# # Extract trigrams from positive_reviews and insert into dictionary
# # (w1, w3) is the key, [ w2 ] are the values
# for review in positive_reviews:
#     s = review.text.lower()
#     tokens = nltk.tokenize.word_tokenize(s)
#     for i in range(len(tokens) - 2):
#         k = (tokens[i], tokens[i+2])
#         if k not in trigrams:
#             trigrams[k] = []
#             trigrams[k].append(tokens[i+1])

# # turn each array of middle-words into a probability vector
# from future.utils import iteritems
# # Initialize an Empty Dictionary
# trigram_probabilities = {} 
# for k, words in iteritems(trigrams):
#     # create a dictionary of word -> count
#     if len(set(words)) > 1:
#         # only do this when there are different possibilities for a middle word
#         d = {}
#         n = 0
#         for w in words:
#             if w not in d:
#                 d[w] = 0
#                 d[w] += 1
#                 n += 1
#                 for w, c in iteritems(d):
#                     d[w] = float(c) / n
#                     trigram_probabilities[k] = d
#                     # choose a random sample from dictionary where values are the 
#                     # probabilities
# def random_sample(d):
#     r = random.random() #Initialize an Empty list
#     cumulative = 0
#     for w, p in iteritems(d):
#         cumulative += p
#         if r < cumulative:
#             return w

# def test_spinner():
#     review = random.choice(positive_reviews)
#     s = review.text.lower()
#     print("Original Text:", s)
#     tokens = nltk.tokenize.word_tokenize(s)
#     for i in range(len(tokens) - 2):
#         if random.random() < 0.2: # 20% chance of replacement
#             k = (tokens[i], tokens[i+2])
#             if k in trigram_probabilities:
#                 w = random_sample(trigram_probabilities[k])
#                 tokens[i+1] = w
#                 print("Spin Text:")
#                 print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))                         
 
# if __name__ == '__main__':
#     test_spinner()

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
import nltk
#nltk.download('wordnet')

from nltk.corpus import wordnet
from nltk.tokenize import regexp_tokenize
import nltk.data
from nltk.stem.porter import *
import random

#an example of how to build a simple text spinner using nltk wordnet corpus
#obviusly you can modify this to work with any other synonym database

class spinner( object ):

#   function to spin spintax text using regex  
#   s = "{Spinning|Re-writing|Rotating|Content spinning|Rewriting} is {fun|enjoyable|entertaining|exciting|enjoyment}! try it {for yourself|on your own|yourself|by yourself|for you} and {see how|observe how|observe} it {works|functions|operates|performs|is effective}."
#   print spin(s)

  def spin(self, s):
    while True:
      s, n = re.subn('{([^{}]*)}',
            lambda m: random.choice(m.group(1).split("|")),
            s)

      if n == 0: break
    return s.strip()  

#  split a paragraph into sentences.
#  you can use the following replace and split functions or the nltk sentence tokenizer
#  content = content.replace("\n", ". ")
#  return content.split(". ")

  def splitToSentences(self, content):
    # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
    return tokenizer.tokenize(content)  

#   get all synonyms of a word from the wordnet database

  def getSynonyms(self, word):
#     include the original word
    synonyms = [word]
    for syn in wordnet.synsets(word):
      for lemma in syn.lemmas():
        if lemma.name != word:
#           since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
          w, n = re.subn("_", " ", lemma.name())
          synonyms.append(w)
    s = list(set(synonyms))
    return len(s), s
  
#   transform text into spintax with the folowing steps
#   1. split the text to sentences
#   2. loop through the sentences and tokenize it
#   3. loop thorugh each token, find its stem and assemble all the synonyms of it into the spintax

  def getSpintax(self, text):
    sentences = self.splitToSentences(text)
    stemmer = PorterStemmer()
    spintax = ""
    for sentence in sentences:
      tokens = regexp_tokenize(sentence, "[\w']+")
      for token in tokens:
        stem = token
        n, syn = self.getSynonyms(stem)
        spintax += "{"
        spintax += token
        spintax += "|"

        for x in range(n):
          spintax += syn[x]
          if x < n-1:
            spintax += "|"
          else:
            spintax += "} "
    return spintax
#---------------------------------end of spinner class ---------------------------------#
if __name__ == '__main__':
# Assign the object for the class
    s = spinner()
    #st = "¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
    st = "¿Hola, cómo estás?. Soy Andrés y quiero que esta vez todo salga bien"
    spintax = s.getSpintax(st)
    print("spintax: ",spintax)
    spun = s.spin(spintax)
    print("spun: ",spun)

# # import nltk
# # #nltk.download('cess_esp')
# # from nltk.corpus import wordnet 
# # from nltk.corpus import PlaintextCorpusReader

# # s = nltk.corpus.cess_esp.words()

# # #nltk.download('stopwords')
# # syns = wordnet.synsets("programa") 
# # print(syns)
# # # syns = PlaintextCorpusReader(syns, '.*', encoding='latin-1')  
# # # print(syns[0].name()) 
  
# # # print(syns[0].lemmas()[0].name()) 
  
# # # print(syns[0].definition()) 
  
# # # print(syns[0].examples())


