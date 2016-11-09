#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
import json
import cabapi

fields_cabinet=['id','name','idc_id','u_num','power']
fields_idc=['id','name','name_cn','address','adminer','phone','num']

@app.route('/cabinet')
def cabinet():
    if not session.get('name'):
        return render_template('login.html')
    username=session.get("name")
    cabinets = cabapi.list('cabinet',fields_cabinet)
    for i in cabinets:
        idc = cabapi.list('idc',fields_idc,i['idc_id'])
        i['idc_id'] = idc['name']

    return render_template("cabinetlist.html",cabinets = cabinets,username=username)
