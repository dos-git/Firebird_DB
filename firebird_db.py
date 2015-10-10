import os, sys
import fdb


DB_NAME = "fb_database.gdb"
FB_DIR = "database"
UT_DIR = "ut"

fb_path = UT_DIR + os.sep + FB_DIR + os.sep + DB_NAME
#DB_NAME = "/tmp/fbdb/fdb_2.db"
path = os.getcwd()

sql_create = "create table CLIENTS (ID INTEGER NOT NULL, COMPANY VARCHAR(50), NAME VARCHAR(50))"

#print path
#path = path + os.sep + DB_NAME
print path
sql = "create database '%s' user 'sysdba' password 'masterkey'" % fb_path
print sql
print fdb.__version__
con = fdb.create_database(sql)
cur = con.cursor()
cur.execute(sql_create)
con.commit()
cur.close()
con.close()
#con.drop_database()


#con = fdb.connect(dsn='/path/database.fdb', user='sysdba', password='masterkey')

print "HELLO WORLD"