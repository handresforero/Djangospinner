import WoobDictionary
from WoobDictionary import synonym_dictionary

sentence = """mambru se fue a la Guerra, que dolor, que dolor, que pena"""
#print(sentence)
h = sentence.replace("."," . ").replace(","," , ").replace(":"," : ").replace(";"," ; ").replace("["," [ ").replace("]"," ] ").replace("{"," { ").replace("}"," } ").replace("|"," | ").replace("!"," ! ").replace("¡"," ¡ ").replace("?"," ? ").replace("¿"," ¿ ").replace("","").replace("'"," ' ").replace('"',' " ').replace("("," ( ").replace(")"," ) ")

tokens = h.split(" ")

sinonyms = []
import random
for t in tokens:        
    word = filter(lambda a: t in a, synonym_dictionary)
    word = list(word)
       
    if len(word) >=1:
        element = word[0]
        l = random.choice(element)        
        sinonyms.append(l)        
    else:
        sinonyms.append(t)

sentence = str(sinonyms)
sentence = sentence.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ")
sentence = sentence[1:]
sentence = sentence[:-1]
print(sentence)  
