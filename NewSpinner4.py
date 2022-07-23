# import WoobDictionary
# from WoobDictionary import synonym_dictionary
# import pymysql

# sentence = """se espera que el mandatario anuncie la decisión durante una alocución en la televisión"""
# #que el mandatario anuncie la decisión durante una alocución en la televisió
# #print(sentence)
# h = sentence.replace("."," . ").replace(","," , ").replace(":"," : ").replace(";"," ; ").replace("["," [ ").replace("]"," ] ").replace("{"," { ").replace("}"," } ").replace("|"," | ").replace("!"," ! ").replace("¡"," ¡ ").replace("?"," ? ").replace("¿"," ¿ ").replace("","").replace("'"," ' ").replace('"',' " ').replace("("," ( ").replace(")"," ) ")

# tokens = h.split(" ")

# databaseServerIP = 'woo.woobsing.net'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'dwX%S7-sg2zA3xnA-56GAw~'          # Password for the database user
# newDatabaseName = 'woobsing_inbound' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# db = pymysql.connect(host=databaseServerIP,
#                     user=databaseUserName,
#                     password=databaseUserPassword,
#                     database=newDatabaseName,
#                     charset=charSet,
#                     cursorclass=cusrorType)
# cursor = db.cursor()
# #word = 'dios'
# #se espera que el mandatario anuncie la decisión durante una alocución en la televisión

# str2 = "None"
# sinonyms = []
# sinonyms1 = []
# sinonyms2 = []
# sinonyms3 = []
# sinonyms4 = []
# sinonyms5 = []

# import random
# for t in tokens:
#     #print(t)
#     cursor.execute("SELECT idPalabra FROM woobsing_inbound.spin_diccionario_palabras WHERE palabra=%s",(t))
#     myresult = cursor.fetchone()
    
#     if str(myresult) == str2:
#         #idpalabra = t
#         sinonyms.append(t)
#        # print(idpalabra)
#     else:
#         idpalabra = myresult['idPalabra']
#         #print(idpalabra)
#         cursor.execute("SELECT idPalabraRel FROM woobsing_inbound.spin_diccionario_sinonimos_por_palabra WHERE idPalabra=%s",(idpalabra))
#         #myresult2 = cursor.fetchall()
#         row = [item['idPalabraRel'] for item in cursor.fetchall()]         

#         listofwords = []
#         for r in row:
#             cursor.execute("SELECT palabra FROM woobsing_inbound.spin_diccionario_palabras WHERE idPalabra=%s",(r))
#             myresult3 = cursor.fetchone()
#             idpalabra3 = myresult3['palabra']
#             listofwords.append(idpalabra3)
#         #print(listofwords)        

#         if len(listofwords) >=1:
#             l = random.choice(listofwords)
#             sinonyms.append(l)
#             m = random.choice(listofwords)
#             sinonyms1.append(m)
#             n = random.choice(listofwords)
#             sinonyms2.append(n)
#             o = random.choice(listofwords)
#             sinonyms3.append(o)
#             p = random.choice(listofwords)
#             sinonyms4.append(p)
#             q = random.choice(listofwords)
#             sinonyms5.append(q)
            
#         else:
#             sinonyms.append(t)
#             sinonyms1.append(t)
#             sinonyms2.append(t)
#             sinonyms3.append(t)
#             sinonyms4.append(t)
#             sinonyms5.append(t)
# #print(sinonyms)

# sentence = str(sinonyms)
# sentence = sentence.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence = sentence[1:]
# sentence = sentence[:-1]

# sentence1 = str(sinonyms1)
# sentence1 = sentence1.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence1 = sentence1[1:]
# sentence1 = sentence1[:-1]

# sentence2 = str(sinonyms2)
# sentence2 = sentence2.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence2 = sentence2[1:]
# sentence2 = sentence2[:-1]

# sentence3 = str(sinonyms3)
# sentence3 = sentence3.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence3 = sentence3[1:]
# sentence3 = sentence3[:-1]

# sentence4 = str(sinonyms4)
# sentence4 = sentence4.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence4 = sentence4[1:]
# sentence4 = sentence4[:-1]

# sentence5 = str(sinonyms5)
# sentence5 = sentence5.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ").replace("  "," ")
# sentence5 = sentence5[1:]
# sentence5 = sentence5[:-1]

# print("resultado1",sentence)
# print("resultado2",sentence1)
# print("resultado3",sentence2)
# print("resultado4",sentence3)
# print("resultado5",sentence4)
# print("resultado6",sentence5)
# db.close()

import pymysql

databaseServerIP = 'woo.woobsing.net'  # IP address of the MySQL database server
databaseUserName = 'aforero'      # User name of the database server
databaseUserPassword = 'dwX%S7-sg2zA3xnA-56GAw~'          # Password for the database user
newDatabaseName = 'woobsing_inbound' # Name of the database that is to be created
charSet = 'utf8mb4'     # Character set
cusrorType = pymysql.cursors.DictCursor

db = pymysql.connect(host=databaseServerIP,
                    user=databaseUserName,
                    password=databaseUserPassword,
                    database=newDatabaseName,
                    charset=charSet,
                    cursorclass=cusrorType)
cursor = db.cursor()
#word = 'dios'
#se espera que el mandatario anuncie la decisión durante una alocución en la televisión



    #print(t)
n = cursor.execute("SELECT idPalabra, sentence FROM woobsing_inbound.spin_diccionario_sinonimos_por_palabra")
myresult = cursor.fetchall()

 