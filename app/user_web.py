#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
import json
import hashlib
import db

salt="www.123"

# 欢迎页面

@app.route("/")
@app.route("/index")
def index():
        username=session.get("name")
        if not username:
                return redirect("/login")
        return render_template("index.html",username=username)

#用户列表

@app.route("/userlist")
def userlist():
#判断用户是否登录，如果没有登录就跳转到登录页
        if not session.get('name'):
                return redirect('/login')
        user_items=["id","name","name_cn","email","mobile","role","status"]
        username=session.get("name")
        if username == "admin":
		table='users'
        	result = db.get_list(user_items,table)
        	data = [dict((k,row[i]) for i,k in enumerate(user_items)) for row in result]
                return render_template("userlist.html",users=data,username=username)


#个人信息

@app.route("/userinfo")
def userinfo():
        if not session.get('name'):
                return redirect('/login')
        username=session.get("name")
        if username == session.get('name'):
		fields = ['id','name','name_cn','mobile','email','role','status']
	        result = db.getone(fields,username)
	        print result
	        users = dict((k,result[i]) for i,k in enumerate(fields))
	        return render_template("userinfo.html",users=users,username=username)


#添加用户
@app.route("/adduser",methods=['GET','POST'])
def adduser():
        if request.method =="GET":
                username=session.get("name")
                return render_template("register.html",username=username)

#前端post请求，逻辑端通过request.form获取整个表单的值
        if request.method =="POST":
                userlist=dict((k,v[0]) for k,v in dict(request.form).items())
                userlist['password']=hashlib.md5(userlist['password']+salt).hexdigest()
                userlist['re_password']=hashlib.md5(userlist['re_password']+salt).hexdigest()
                if userlist["name"] in [ n.values()[0] for n in get_userlist(["name"]) ]:
                        errmsg = "username is exist"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if not userlist["name"] or not userlist["password"]:
                        errmsg = "username and password is not empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if userlist["password"] != userlist["re_password"]:
                        errmsg="password is error"
                        return json.dumps({'code':'1','errmsg':errmsg})
                fields = ["name","name_cn","password","mobile","email","role","status"]
                values = [ '%s'%userlist[x] for x in fields]
                userdict = dict([(k,values[i]) for i,k in enumerate(fields)])
                add_user(userdict)
                return json.dumps({'code':'0','result':"register sucess"})

#删除用户

@app.route("/deluser",methods=['POST'])
def deluser():
        if not session.get('name'):
                return redirect('/login')
#前端get请求，逻辑端通过request.args.get获取参数
        uid=request.args.get("uid")
	table='users'
        print uid
        db.delete(table,uid)
        return json.dumps({"code":0,"result":"delete user success"})


#更新用户

@app.route("/update",methods=['GET','POST'])
def updateuser():
    table = 'users'
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
        print data
        condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
        print condition
        db.update(condition, data['id'][0], table)
        return json.dumps({'code':0,'result':'update user success'})
    else:
        id = request.args.get('uid')
	print id
        fields = ['id', 'name', 'name_cn', 'email', 'mobile']
        res = db.selectId(fields,id,table)
        user = dict((k,res[i]) for i,k in enumerate(fields))
        return json.dumps(user)


#修改密码

@app.route("/modpasswd",methods=["POST"])
def changepass():
        if request.method=="POST":
                passwd_info=dict((k,v[0]) for k,v in dict(request.form).items())
                print passwd_info
                if len(passwd_info) == 3:
                        if passwd_info["password"] != passwd_info["re_password"]:
                                return json.dumps({"code":1,"errmsg":"The tow password is different"})
                if not passwd_info.get("password","None") or not passwd_info.get("re_password","None"):
                        errmsg = "password can not be empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
                else:
                        uid=passwd_info["id"]
                        password=passwd_info["password"]
                        modpasswd(password,uid)
                        return json.dumps({'code':'0','result':"change sucess"})

