#!/usr/bin/python
#coding:utf-8

from flask import Flask

app = Flask(__name__)
app.secret_key='www.123'

import user_web,cmdb,login
