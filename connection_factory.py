# -*- coding: UTF-8 -**
import MySQLdb

class Connection_factory(object):
    def get_connection(self):
        return MySQLdb.connect(
            host='localhost',
            user='root',
            pass='',
            db='alura'
        )