import os, sys
import fdb


# Info about Firebird (Fb)
# After installation there is created user firebird
# Fb db could be created only in a dir owned by firebird user
# GSEC is command line tool for Fb administrative purpose, manages creation/removing users, also manges change of
# user's password etc.
# Fb db run as server which needs to run before any db operation is performed

DB_NAME = "fb_database.gdb"
FB_DIR = "database"
UT_DIR = "ut"


fb_path = UT_DIR + os.sep + FB_DIR + os.sep + DB_NAME
full_path = os.getcwd() + os.sep + fb_path

sql_select_all = "select * from CLIENTS"
# FIELD LENGHT makes error -maybe because there is no entries in db
#sql_select_struct = "SELECT RDB$FIELD_NAME, RDB$DESCRIPTION, RDB$DEFAULT_VALUE, RDB$NULL_FLAG, RDB$FIELD_LENGTH FROM RDB$RELATION_FIELDS WHERE RDB$RELATION_NAME='CLIENTS';"
sql_select_struct = "SELECT RDB$FIELD_NAME, RDB$DESCRIPTION, RDB$DEFAULT_VALUE, RDB$NULL_FLAG FROM RDB$RELATION_FIELDS WHERE RDB$RELATION_NAME='CLIENTS';"
sql_create_db = "create database '%s' user 'sysdba' password 'masterkey'" % fb_path
sql_create_table_1 = "create table CLIENTS (ID_client INTEGER NOT NULL, COMPANY VARCHAR(20), NAME VARCHAR(20))"
sql_create_table_2 = "create table ITEMS (ID_item INTEGER NOT NULL, NAME VARCHAR(50), PRIZE INTEGER NOT NULL, CREATE_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"

# full_path is not seen because script is run as dos user - only connection to db is done as firebird user
#if os.path.exists(full_path):
con = None
cur = None
try:
    con = fdb.create_database(sql_create_db)
    #con = fdb.connect(dsn=fb_path, user='sysdba', password='masterkey')
    cur = con.cursor()
    cur.execute(sql_create_table_1)
    con.commit()    # commit is a part of table creation, without it, table will not be created
    #cur.execute(sql_create_table_2)
    #con.commit()    # commit is a part of table creation, without it, table will not be created

    data = cur.execute(sql_select_struct)
    print data.fetchall()

except fdb.DatabaseError as e:
    print "[0] %s" % str(e.args[0])
    print "[1] %s" % str(e.args[1])
    print "[2] %s" % str(e.args[2])

finally:
    if con:
        print "CLOSE CONNECTION"
        cur.close()
        con.close()
#con.drop_database()


#con = fdb.connect(dsn='/path/database.fdb', user='sysdba', password='masterkey')

