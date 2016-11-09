#!/usr/bin/env python
#coding:utf-8
import MySQLdb as mysql
conn=mysql.connect(user='root',passwd='www.123',db='reboot10',charset='utf8')
curs=conn.cursor()
conn.autocommit(True)

#获取列表

def get_list(listitem,table):
        sql="select %s from %s" %(','.join(listitem),table)
        curs.execute(sql)
        result=curs.fetchall()
	return result

#获取单个用户

def getone(fields,condition):
       sql = "SELECT %s FROM users WHERE name='%s'" % (','.join(fields), condition)
       curs.execute(sql)
       res = curs.fetchone()
       return res



#添加用户

def add_user(userlist):
	sql="insert into users(%s)values('%s')"%(",".join(userlist.keys()),"','".join(userlist.values()))
        curs.execute(sql)
        conn.commit()

#删除

def delete(table,uid):
        sql = "DELETE FROM %s WHERE id = %s" % (table,uid)
        curs.execute(sql)

#更新

def update(condition,uid,table):
    sql = "UPDATE %s SET %s WHERE id = %s" % (table, ','.join(condition), uid)
    curs.execute(sql)


def selectId(fields,uid,table):
    sql = "SELECT %s FROM %s WHERE id = %s" % (','.join(fields), table, uid)
    curs.execute(sql)
    res = curs.fetchone()
    return res


#修改密码
def modpasswd(password,uid):
    sql = "update users set password='%s' where id='%s'"%(password,uid)
    curs.execute(sql)
    conn.commit()


#添加idc

def add_idc(idclist):
        sql="insert into idclist(%s)values('%s')"%(",".join(idclist.keys()),"','".join(idclist.values()))
        curs.execute(sql)
        conn.commit()


