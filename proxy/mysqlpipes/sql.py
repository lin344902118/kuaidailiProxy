#coding:utf-8
import MySQLdb
from proxy import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB


class Sql(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host=MYSQL_HOSTS, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB)
        self.cur = self.conn.cursor()

    def insert_dd_name(self, ip, port, status, ip_type, address, speed, last_validate_time):
        sql = 'insert into kuaidaili (ip, port, status, ip_type, address, speed, last_validate_time) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' %(ip, port, status, ip_type, address, speed, last_validate_time)
        print sql
        self.conn.set_character_set('utf8')
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')
        self.cur.execute(sql)
        self.conn.commit()

    def select_dd_name(self, ip):
        sql = 'select exists(select 1 from kuaidaili where ip="%s")' %ip
        print sql
        self.cur.execute(sql)
        return self.cur.fetchall()[0]