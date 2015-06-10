import MySQLdb

conn = MySQLdb.connect(host= "localhost", user="root",passwd="",db="traffic_providor")
x = conn.cursor()
with open(fname) as f:
    content = f.readlines()

for l in content :
	l = exploide(":", l)[1];
	l = exploide(" ") ; 
	ip = l[0];
	port = l[1] ;
	extra = l[2] ;
    try:
     	x.execute("""INSERT INTO ips VALUES (%s,%s)""",(0,90))
   		conn.commit()
	except:
   		conn.rollback()

conn.close()