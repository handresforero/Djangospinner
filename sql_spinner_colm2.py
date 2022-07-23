#D:\Woobsing\LongTail
#conda activate ppSpinner

from base64 import encode
import pymysql
import re
from timeit import default_timer
import pandas as pd
from csv import reader

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
databaseUserName = 'aforero'      
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
newDatabaseName = 'LongTail' 
charSet = 'utf8mb4'     
cusrorType = pymysql.cursors.DictCursor
db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
cursor = db.cursor()

# ## ADD NEW COLUMN    #######################################################################################  
# cursor.execute("ALTER TABLE LongTail.ParseContent ADD textSpinned2 longtext")
# #cursor.execute("ALTER TABLE LongTail.LongTailTable4 ADD id_Key INT PRIMARY KEY AUTO_INCREMENT") #add primary key and consecutive values
# db.commit()    
# myresult = cursor.fetchall()
# db.close()
# print("NEW COLUMN ADDED..")

### DOWNLOAD    #######################################################################################
#cursor.execute("SELECT id_Key, parrafos FROM LongTail.ParseContent WHERE id_Key=1")
# cursor.execute("SELECT id_Key, parrafos FROM LongTail.ParseContent WHERE parrafos LIKE '%Si el artículo incluso así no existe%'")
# myresult = cursor.fetchall()
# print(myresult)
# ErrorList = []
# Resultados = open("Resultados.csv", "a", encoding='utf8')
# for row in myresult:
#     ErrorList.append(str(row))
#     #ErrorList.append(str(errorDescr))
#     ErrorList.append("\n")  
#     Resultados.write("|".join(ErrorList))
# Resultados.close
# cursor.close
from bs4 import BeautifulSoup
import requests
from timeit import default_timer
import re
import random
import itertools
import spacy
# CMBIAR COTENIDO DE COLUMNAS ################################################
# i = []
# inicio = default_timer()

# for p in i:
#     cursor.execute("SELECT urls FROM LongTail.ParseContent WHERE id_Key= %s",(p))
#     myresult = cursor.fetchone()
#     listOfValues = myresult.values()
#     listOfValues = list(listOfValues)
#     listOfValues = str(listOfValues[0])
#     result = listOfValues[:-1]
#     cursor.execute("UPDATE LongTail.ParseContent SET urls = %s WHERE id_Key= %s",(result,p))
#     cursor.execute("SELECT urls FROM LongTail.ParseContent WHERE id_Key= %s",(p))
#     myresult1 = cursor.fetchone()
#     db.commit()
#     print(myresult1)
    
#     print(p)
#     inicio2 = default_timer()
#     cursor.execute("SELECT urls FROM LongTail.ParseContent WHERE id_Key= %s",(p))
#     myresult = cursor.fetchone()
#     listOfValues = myresult.values() #convertir valores de diccionario a lista
#     listOfValues = list(listOfValues)
#     listOfValues = str(listOfValues[0])
#     print(listOfValues)
#     fin1 = default_timer()
#     print("URL obtenida: ", fin1 - inicio2)
             
#     url = listOfValues

#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
       
#     fin2 = default_timer()
#         print("html obtenido: ", fin2 - fin1)
        
#     text = []
#     for idx, item in enumerate(soup.find_all("p")):
#         text.append(item.text)
#     text = str(text)
#         print(text)
       
#     fin3 = default_timer()
#         print("parseado: ", fin3 - fin2)        
#     cursor.execute("UPDATE LongTail.ParseContent SET parrafos = %s WHERE id_Key= %s",(text,p))                
#     cursor.execute("SELECT parrafos FROM LongTail.ParseContent WHERE id_Key= %s",(p))
#     myresult1 = cursor.fetchone()
#     db.commit()
#     print(myresult1) 
import spacy
import PyMultiDictionary
from PyMultiDictionary import MultiDictionary
import re
import random
import itertools

i = 137

while i <= 10500:
    
    cursor.execute("SELECT parrafos FROM LongTail.ParseContent WHERE id_Key= %s",(i))
    myresult = cursor.fetchone()
    listOfValues = myresult.values()
    listOfValues = list(listOfValues)
    listOfValues = str(listOfValues[0])
    sentences = listOfValues
    
    sentences = sentences.replace("'",'"').replace("[","").replace("]","")
    sentences = sentences[1:]
    #print(sentences)
    
    #print("1er sentence:", sentences)
           
    
    #python -m spacy download es

    nlp = spacy.load("es_core_news_sm")
    #sentences = "donde se encuentra popeye"
    doc = nlp(sentences)
    tokens = [token for token in doc]
    tokens = tokens[0:100]
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
    print(sinonyms)
    # # s = tokens.append(word)
    # # print(s)

    sentence = str(sinonyms)
    #print(sentence)

    sentence = sentence.replace("['","|").replace("']","").replace("[","{").replace("]", "}").replace(",,", "°°°").replace(",", "").replace(" ?", "?").replace("¿ ", "¿").replace(" !", "!").replace("¡ ", "¡").replace("", "").replace("' '", "|").replace("'", "").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace("( ", "(").replace(" )", ")")
    sentence = sentence.replace("°°°",",").replace(" ,", ",")
    sentence = sentence[1:]
    sentence = sentence[:-1]
    #sentence = sentence.lstrip("{").rstrip("}")
    print("Texto arreglado",sentence)

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
    #print("Texto spinedo: ",spin)
    #print("Registro Terminado: ",i)
    spin = str(spin)
    
    cursor.execute("UPDATE LongTail.ParseContent SET textSpinned2 = %s WHERE id_Key= %s",(spin,i))                
    cursor.execute("SELECT textSpinned2 FROM LongTail.ParseContent WHERE id_Key= %s",(i))
    myresult1 = cursor.fetchone()
    print(myresult1)
    
    db.commit()
    
    print("Texto terminado: ",i)
    i += 1

 
cursor.close()
    
