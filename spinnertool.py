import pywebio
from pywebio.input import input, TEXT 
from pywebio.output import put_text, put_html, put_markdown, put_table
from pywebio import start_server
import argparse



def bmi():
    sentences = input("Ingrese el texto a Spinnear：", type=TEXT)
    
    import spacy
    #python -m spacy download es

    nlp = spacy.load("es_core_news_sm")
    #sentences = "Quiero cantar. Aveces quisiera decir !hola!, pero digo 'Helo', entonces me pregunto si estoy en lo correcto o no."
    doc = nlp(sentences)
    tokens = [token for token in doc]
    #print(tokens)

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

    sentence = str(sinonyms)


    sentence = sentence.replace("['","|").replace("']","").replace("[","{").replace("]", "}").replace(",,", "°°°").replace(",", "").replace(" ?", "?").replace("¿ ", "¿").replace(" !", "!").replace("¡ ", "¡").replace("", "").replace("' '", "|").replace("'", "").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace("( ", "(").replace(" )", ")")
    sentence = sentence.replace("°°°",",").replace(" ,", ",")
    sentence = sentence.lstrip("{").rstrip("}")
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

    email = '"""'+sentence+'"""'
    spin = spintax(sentence)
    #spin = spintax(email, single=False)
    #print(spin)  
    
          
    #tabla_url = df1.pivot_table(columns=[' urls '], aggfunc='size')    

    for common in spin:
                
        #put_markdown('# **Resultados**')
        #put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
        #put_html('<br><br>')
        
        put_markdown('# **Resultados de la búsqueda**').style('color: red; font-size: 30px')
        put_text('Powered by Woobsing').style('color: grey; font-size: 10px')
        #put_html('<br>Los siguientes son datos obtenidos de la base Elnoti<br>')        
        put_text('Resultado spineado')
            
            
        #put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
        put_html('<hr>')
        put_table([
        #['Dominio', 'URL'],
        [spin],
        ])

        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    
    start_server(bmi, port=args.port)
    #pywebio.start_server(bmi, port=80)