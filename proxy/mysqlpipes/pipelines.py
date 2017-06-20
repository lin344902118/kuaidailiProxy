#coding:utf-8
import traceback
import datetime
from .sql import Sql



class KuaidailiPipeLine(object):

    def process_item(self, item, spider):
        sql = Sql()
        try:
            ip = item['ip'][0].strip().decode()
            ret = sql.select_dd_name(ip)
            if ret[0] == 1:
                print 'exists'
            else:
                port = item['port'][0].strip().decode()
                status = item['status'][0].strip().decode()
                ip_type = item['type'][0].strip().decode()
                address = item['address'][0].strip().decode()
                speed = item['speed'][0].strip().decode()
                last_validate_time = datetime.datetime.strptime(item['last_validate_time'][0], '%Y-%m-%d %H:%M:%S')
                sql.insert_dd_name(ip, port, status, ip_type, address, speed, last_validate_time)
                print 'save'
        except Exception, e:
            print e
            print traceback.format_exc()
        finally:
            sql.cur.close()
            sql.conn.close()