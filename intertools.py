# # # import re
# # # import random
# # # import itertools

# # # def spintax(text, single=True):
# # #     """Return a list of unique spins of a Spintax text string.

# # #     Args:
# # #         text (string): Spintax text (i.e. I am the {President|King|Ambassador} of Nigeria.)
# # #         single (bool, optional): Optional boolean to return a list or a single spin.

# # #     Returns:
# # #         spins (string, list): Single spin or list of spins depending on single.
# # #     """

# # #     pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
# # #     chunks = pattern.split(text)

# # #     def options(s):
# # #         if len(s) > 0 and s[0] == '{':
# # #             return [opt for opt in s[1:-1].split('|')]
# # #         return [s]

# # #     parts_list = [options(chunk) for chunk in chunks]

# # #     spins = []

# # #     for spin in itertools.product(*parts_list):
# # #         spins.append(''.join(spin))

# # #     if single:
# # #         return spins[random.randint(0, len(spins)-1)]
# # #     else:
# # #         return spins

# # # email = """Yo soy andrés!!. {Bakare|George|Mutassim|John} Tunde, the {son|father|brother|cousin} of Nigerian {astronaut|biochemist|major|general|prime minister|ambassador} {Abacha} Tunde."""
# # # #spin = spintax(email)
# # # #spin = spintax(email, single=False)
# # # #print(spin)



# # # # import PyMultiDictionary
# # # # from PyMultiDictionary import MultiDictionary
# # # # dictionary = MultiDictionary()
# # # # print(dictionary.synonym('es', 'cantar'))

# # import re
# # import random
# # import itertools

# # def spintax(text, single=True):
# #     """Return a list of unique spins of a Spintax text string.

# #     Args:
# #         text (string): Spintax text (i.e. I am the {President|King|Ambassador} of Nigeria.)
# #         single (bool, optional): Optional boolean to return a list or a single spin.

# #     Returns:
# #         spins (string, list): Single spin or list of spins depending on single.
# #     """

# #     pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
# #     chunks = pattern.split(text)

# #     def options(s):
# #         if len(s) > 0 and s[0] == '{':
# #             return [opt for opt in s[1:-1].split('|')]
# #         return [s]

# #     parts_list = [options(chunk) for chunk in chunks]

# #     spins = []

# #     for spin in itertools.product(*parts_list):
# #         spins.append(''.join(spin))

# #     if single:
# #         return spins[random.randint(0, len(spins)-1)]
# #     else:
# #         return spins

# # email = """Yo soy andrés!!. {Bakare|George|Mutassim|John} Tunde, the {son|father|brother|cousin} of Nigerian {astronaut|biochemist|major|general|prime minister|ambassador} {Abacha} Tunde."""
# # #spin = spintax(email)
# # #spin = spintax(email, single=False)
# # #print(spin)



# # # import PyMultiDictionary
# # # from PyMultiDictionary import MultiDictionary
# # # dictionary = MultiDictionary()
# # # print(dictionary.synonym('es', 'cantar'))

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

import spacy
#python -m spacy download es

# nlp = spacy.load("es_core_news_sm")
# sentences = "donde se encuentra popeye"
# doc = nlp(sentences)
# tokens = [token for token in doc]
# #print(tokens)

# import PyMultiDictionary
# from PyMultiDictionary import MultiDictionary
# dictionary = MultiDictionary()
# sinonyms = []
# for t in tokens:
#     #print(t)
#     word = dictionary.synonym('es', str(t))
#     if len(word) >=1:
#         l = []
#         l.append(t)
#         l.append(word)
#         sinonyms.append(l)
#         #sinonyms.append(word)
#     else:
#         sinonyms.append(t)
# #print(sinonyms)
# # s = tokens.append(word)
# # print(s)

# sentence = str(sinonyms)
# #print(sentence)

# sentence = sentence.replace("['","|").replace("']","").replace("[","{").replace("]", "}").replace(",,", "°°°").replace(",", "").replace(" ?", "?").replace("¿ ", "¿").replace(" !", "!").replace("¡ ", "¡").replace("", "").replace("' '", "|").replace("'", "").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace("( ", "(").replace(" )", ")")
# sentence = sentence.replace("°°°",",").replace(" ,", ",")
# sentence = sentence[1:]
# sentence = sentence[:-1]
# #sentence = sentence.lstrip("{").rstrip("}")
# #print(sentence)





# import re
# import random
# import itertools

# def spintax(text, single=True):
#     """Return a list of unique spins of a Spintax text string.

#     Args:
#         text (string): Spintax text (i.e. I am the {President|King|Ambassador} of Nigeria.)
#         single (bool, optional): Optional boolean to return a list or a single spin.

#     Returns:
#         spins (string, list): Single spin or list of spins depending on single.
#     """

#     pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
#     chunks = pattern.split(text)

#     def options(s):
#         if len(s) > 0 and s[0] == '{':
#             return [opt for opt in s[1:-1].split('|')]
#         return [s]

#     parts_list = [options(chunk) for chunk in chunks]

#     spins = []

#     for spin in itertools.product(*parts_list):
#         spins.append(''.join(spin))

#     if single:
#         return spins[random.randint(0, len(spins)-1)]
#     else:
#         return spins

# #email = '"""'+sentence+'"""'
# spin = spintax(sentence)
# #spin = spintax(email, single=False)
# print(spin)
sentences = "un concurso de interacción social que premia a los usuarios más activos en sus redes, vuélvete un influencer utilizando tus redes sociales, por cada interaccion ganas puntos"
#print(sentences)
nlp = spacy.load("es_core_news_sm")
    #sentences = "Quiero cantar. Aveces quisiera decir !hola!, pero digo 'Helo', entonces me pregunto si estoy en lo correcto o no."
doc = nlp(sentences)
tokens = [token for token in doc]
#print(tokens)
# #tokens = tokens[0:52]
print("tokens: ",tokens)
import PyMultiDictionary
from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()
sinonyms = []
for t in tokens:
        #print(t)
    word = dictionary.synonym('es', str(t))
    if len(word) >=1:
        l = []
        l.append(t)
        l.append(word)
        sinonyms.append(l)
            #sinonyms.append(word)
    else:
        sinonyms.append(t)
    #print(sinonyms)
    # s = tokens.append(word)
    # print(s)
print("sinonimos",sinonyms)
sentence = str(sinonyms)
# print(sentence)


sentence = sentence.replace("['","|").replace("']","").replace("[","{").replace("]", "}").replace(",,", "°°°").replace(",", "").replace(" ?", "?").replace("¿ ", "¿").replace(" !", "!").replace("¡ ", "¡").replace("", "").replace("' '", "|").replace("'", "").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace("( ", "(").replace(" )", ")")
sentence = sentence.replace("°°°",",").replace(" ,", ",")
sentence = sentence[1:]
sentence = sentence[:-1]
    #print(sentence)

import re
import random
import itertools

def spintax(text, single=True):
    """Return a list of unique spins of a Spintax text string.

    Args:
        text (string): Spintax text (i.e. I am the {President|King|Ambassador} of Nigeria.)
        single (bool, optional): Optional boolean to return a list or a single spin.

    Returns:
        spins (string, list): Single spin or list of spins depending on single.
    """

    pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
    chunks = pattern.split(text)

    def options(s):
        if len(s) > 0 and s[0] == '{':
            return [opt for opt in s[1:-1].split('|')]
        return [s]

    parts_list = [options(chunk) for chunk in chunks]

    spins = []

    for spin in itertools.product(*parts_list):
        spins.append(''.join(spin))

    if single:
        return spins[random.randint(0, len(spins)-1)]
    else:
        return spins

#email = '"""'+sentence+'"""'
spin = spintax(sentence)
print(spin)
