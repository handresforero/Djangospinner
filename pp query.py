import pymysql

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
databaseUserName = 'aforero'      
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
newDatabaseName = 'LongTail' 
charSet = 'utf8mb4'     
cusrorType = pymysql.cursors.DictCursor
db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
cursor = db.cursor()
word = "%noticias%"

cursor.execute("SELECT urlPagina, textSpinned2 FROM LongTail.ParseContent WHERE urlPagina LIKE %s",(word))
myresult = cursor.fetchall()

print(myresult)
# spin1 = str(myresult)
# print(spin1)