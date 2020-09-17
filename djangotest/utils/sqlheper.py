import pymysql

class SqlHeper():
    def __init__(self):
        self.conn_data()

    def conn_data(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='test',charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def insert_data(self,sql,arg):
        self.cursor.execute(sql,arg)
    def insert_many_data(self,sql,arg):
        self.cursor.executemany(sql, arg)

    def lastrowid(self,sql,arg):
        self.cursor.execute(sql, arg)
        self.commit_data()
        return self.cursor.lastrowid

    def delete_data(self,sql,arg):
        self.cursor.execute(sql,arg)

    def updata_data(self,sql,arg):
        self.cursor.execute(sql,arg)

    def updata_many_data(self,sql,arg):
        self.cursor.executemany(sql,arg)

    def select_all_data(self,sql,arg):
        self.cursor.execute(sql, arg)
        result = self.cursor.fetchall()
        return result

    def select_one_data(self,sql,arg):
        self.cursor.execute(sql,arg)
        result = self.cursor.fetchone()
        return result

    def commit_data(self):
        self.conn.commit()

    def close_data(self):
        self.conn.close()