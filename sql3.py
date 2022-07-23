import pymysql

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
databaseUserName = 'aforero'      
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
newDatabaseName = 'LongTail' 
charSet = 'utf8mb4'     
cusrorType = pymysql.cursors.DictCursor
db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
cursor = db.cursor()


cursor.execute("SELECT idbefore FROM LongTail.ParseContent")
myresult = cursor.fetchall()

for tdict in myresult:    # To iterate over all dictionaries present in the list
    # print tdict
    for key in tdict:    # To iterate over all the keys in current dictionary
        # print key
        number = tdict[key]
        cursor.execute("SELECT urlPagina FROM LongTail.LongTailTable4 WHERE id_Key= %s",(number))
        myresult = cursor.fetchone()
        myresult = myresult['urlPagina']
        
        cursor.execute("UPDATE LongTail.ParseContent SET urlPagina = %s WHERE idbefore= %s",(myresult,number))
        db.commit()
        print(number)
cursor.close()

#print(myresult)


# i=1

# while i <= 1:
    
    
#     cursor.execute("SELECT urlPagina FROM LongTail.LongTailTable4 WHERE id_Key= %s",(i))
#     myresult = cursor.fetchone()
#     myresult = myresult['urlPagina']
        
#     cursor.execute("SELECT urlPagina FROM LongTail.ParseContent WHERE idbefore= %s",(i))
    
#     i += 1
# cursor.close()

