import pymysql

databaseServerIP = 'woo.woobsing.net'  # IP address of the MySQL database server
databaseUserName = 'aforero'      # User name of the database server
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
newDatabaseName = 'LongTail' # Name of the database that is to be created
charSet = 'utf8mb4'     # Character set
cusrorType = pymysql.cursors.DictCursor

db = pymysql.connect(host=databaseServerIP,
                    user=databaseUserName,
                    password=databaseUserPassword,
                    database=newDatabaseName,
                    charset=charSet,
                    cursorclass=cusrorType)