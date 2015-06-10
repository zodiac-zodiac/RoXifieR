import MySQLdb
conn = MySQLdb.connect(host= "localhost", user="root",passwd="",
                  db="traffic_providor")
x = conn.cursor()

try:
   x.execute("""INSERT INTO ips VALUES (%s,%s)""",(0,90))
   conn.commit()
except:
   conn.rollback()

conn.close()