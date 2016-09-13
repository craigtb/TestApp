import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor(dictionary=True);

query = ("SELECT * FROM test.post")

cursor.execute(query)
'''for (name, message) in cursor :
     print name
     print message
'''
res = []
for x in cursor :
     res.append(x)
print res
cnx.close()
