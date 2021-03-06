import pymysql


class database:

    def __init__(self, username, password,birthday):
        self.username = username
        self.password = password
        db = pymysql.connect(host='localhost', user=username, password=password, use_unicode=True, charset="utf8")
        cur = db.cursor()

        sql = 'CREATE DATABASE  IF NOT EXISTS FB_DATA'
        cur.execute(sql)

        sql = 'USE FB_DATA'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS USER(ID NUMERIC(50) PRIMARY KEY,' \
              'NAME CHAR(25) NOT NULL,' \
              'LOCATION CHAR(40),' \
              'GENDER CHAR(10) NOT NULL,' \
              'BIRTHDAY NUMERIC(5))'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS MOVIES(MID NUMERIC(50) PRIMARY KEY,' \
              'MNAME CHAR(25) NOT NULL)'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS MUSIC(SID NUMERIC(50) PRIMARY KEY,' \
              'SNAME CHAR(25) NOT NULL)'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS LIKES(LID NUMERIC(50) PRIMARY KEY,' \
              'LNAME CHAR(25) NOT NULL)'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS INTERESTEDMOVIES(ID NUMERIC(50),' \
              'MID NUMERIC(50),' \
              'FOREIGN KEY(MID) REFERENCES MOVIES(MID),' \
              'PRIMARY KEY(ID,MID))'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS INTERESTEDMUSIC(ID NUMERIC(50),' \
              'SID NUMERIC(50),' \
              'FOREIGN KEY(SID) REFERENCES MUSIC(SID),' \
              'PRIMARY KEY(ID,SID))'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS LIKEDPAGES(ID NUMERIC(50),' \
              'LID NUMERIC(50),' \
              'FOREIGN KEY(LID) REFERENCES LIKES(LID),' \
              'PRIMARY KEY(ID,LID))'

        cur.execute(sql)

    def Insert_User(self,id, name, location, gender,birthday):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE FB_DATA'
        cur.execute(sql)
        sql = "INSERT INTO USER(ID,NAME,LOCATION,GENDER,BIRTHDAY) VALUES(" + str(
            id) + ",'" + name + "','" + location + "','" + gender + "','" + str(birthday) + "')"
        cur.execute(sql)
        db.commit()

    def Movie_Data(self,id,mid, mname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE FB_DATA'
        cur.execute(sql)
        sql = "INSERT INTO MOVIES(MID,MNAME) VALUES(" + str(mid) + ",'" + mname + "')"
        cur.execute(sql)
        sql="INSERT INTO INTERESTEDMOVIES(ID,MID)VALUES(" + str(id) + "," + str(mid) + " )"
        cur.execute(sql)
        db.commit()

    def Music_Data(self,id,sid, sname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE FB_DATA'
        cur.execute(sql)
        sql = "INSERT INTO MUSIC(SID,SNAME) VALUES(" + str(sid) + ",'" + sname + "')"
        cur.execute(sql)
        sql = "INSERT INTO INTERESTEDMUSIC(ID,SID)VALUES(" + str(id) + "," + str(sid) + " )"
        cur.execute(sql)
        db.commit()

    def Pages_Data(self,id,lid, lname):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password)
        cur = db.cursor()
        sql = 'USE FB_DATA'
        cur.execute(sql)
        sql = "INSERT INTO LIKES(LID,LNAME) VALUES(" + str(lid) + ",'" + lname + "')"
        cur.execute(sql)
        sql = "INSERT INTO LIKEDPAGES(ID,LID)VALUES(" + str(id) + "," + str(lid) + " )"
        cur.execute(sql)
        db.commit()
