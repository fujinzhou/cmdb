#!/usr/bin/env python
#coding:utf-8
import  MySQLdb as mysql

conn = mysql.connect(user='root',passwd='www.123',host='localhost',db='reboot10')
conn.autocommit(True)

# 使用with语句，它会判断当前是否有错误，有错误就会回滚，没有就进行事务提交
with conn as cur:
    def list(table,fields,id=None):
	users = []
	if not id:
	    sql = "select %s from %s"%(','.join(fields),table)
	    cur.execute(sql)
	    result = cur.fetchall()
	    for row in result:
		user = {}
		for i,k in enumerate(fields):
		    user[k] = row[i]
		users.append(user)
	    return users
	else:
	    sql2 = "select %s from %s where id='%s'"%(','.join(fields),table,id)
	    print sql2
	    cur.execute(sql2)
	    result = cur.fetchone()
	    print result
	    user = {}
	    for i,k in enumerate(fields):
		user[k] = result[i]
	    return user

    def add(table,args):
	sql = 'insert into %s set %s'%(table,','.join(args))
	cur.execute(sql)
	
    def delete(table,id):
	sql = "delete from %s where id='%s'"%(table,id)
	cur.execute(sql)

    def update(table,args,id):
	sql = "update %s set %s where id=%s"%(table,','.join(args),id)
	cur.execute(sql)
