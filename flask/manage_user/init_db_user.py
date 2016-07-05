import MySQLdb as my

db = my.connect("localhost","root","password","test")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS USER")
sql = """CREATE TABLE user (
	USER_ID  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	FIRST_NAME CHAR(20),
	LAST_NAME CHAR(20),
	USER_NAME CHAR(20) NOT NULL,
	PASSWORD VARCHAR(100) NOT NULL,
	EMAIL VARCHAR(100) NOT NULL) """
cursor.execute(sql)

db.close()
