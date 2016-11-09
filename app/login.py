#!/usr/bin/env python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
import json
import hashlib
import db

salt="www.123"

# 登录

@app.route("/login",methods=['GET','POST'])
def login():
        if request.method =="GET":
                return render_template("login.html")
        if request.method =='POST':
                data = dict((k,v[0]) for k,v in dict(request.form).items())
	        if not data.get('name',None) or not data.get('password',None):
        	    return json.dumps({'code':1,'errmsg':'name or password empty'})
		fields = ['name','password','status']
                name=data["name"]
                userlists = db.getone(fields,name)
		if not userlists:
			return json.dumps({'code':1,'result':'name not exist'})
		user = dict((k,userlists[i]) for i,k in enumerate(fields))
                data['password']=hashlib.md5(data['password']+salt).hexdigest()
                if data["password"] != user['password']:
                        errmsg = "password is error"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if int(user['status'])==1:
                        return json.dumps({'code':'1','errmsg':"账户被锁定"})

#判断session中的用户名与表单里面的用户名是否相同
                session['name']=user['name']
                return json.dumps({'code':'0','result':"login sucess"})




#退出


@app.route('/loginout')
def loginout():
#session是一个大字典，把当前页面对应的session移除
        session.pop('name')
        return redirect('/login')
