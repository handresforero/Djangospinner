
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render
import pymysql


def saludo(request):
    nombre="Juan"
    doc_externo=open("/home/aforero/demoDjango/myDjangoProject/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":nombre})
    documento=plt.render(ctx)
    return HttpResponse(documento)



def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculadora(request):
      
    return render(request, "miplantilla.html")

def home(request):
    return render(request, "home.html")

def homes(request):
    p1=Persona("Profesor Juan", "Díaz")
    temasdelcurso=["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    ahora=datetime.datetime.now()
    doc_extertno=loader.get_template('miplantilla.html')
    documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasdelcurso})
    return HttpResponse(documento)

def submitquery(request):
    q = request.GET['query']
    try:
        ans = q
	
        spin = ans+""
        spin1 = ans+""
        
        databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
        databaseUserName = 'aforero'      
        databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
        newDatabaseName = 'LongTail' 
        charSet = 'utf8mb4'     
        cusrorType = pymysql.cursors.DictCursor
        db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
        cursor = db.cursor()
        
        word = ("%"+q+"%")

        cursor.execute("SELECT urlPagina, domain, textSpinned2 FROM LongTail.ParseContent WHERE urlPagina LIKE %s",(word))
        myresult = cursor.fetchall()
        #print(myresult)
        spin1 = str(myresult)
        spin1 = spin1.replace("urlPagina","Palabras asociadas al resultado").replace("'textSpinned2'","").replace("\\\\n","") 
        
        #.replace("","")  \\\\n

        mydictionary = {
            "q" : q,
            "ans1" : ans,
            "ans2" : spin,
            "ans3" : spin1,
            "error" : False,
            "result" : True
        }
        return render(request, 'home.html',context=mydictionary)
    except:
        mydictionary = {
            "error" : True,
            "result" : False 
        }
        return render(request, 'home.html',context=mydictionary)
    
    

    
