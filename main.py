# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 3:42 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

import app
import os

import pymysql

def connect_db():
    return pymysql.connect(host=os.environ['MYSQL_HOST_NAME'],
                           port=int(os.environ['MYSQL_PORT']),
                           user=os.environ['MYSQL_USER_NAME'],
                           password=os.environ['MYSQL_USER_PASSWORD'],
                           charset='utf8mb4')


con = connect_db()
cur = con.cursor()
sql = f"""CREATE DATABASE IF NOT EXISTS {os.environ['MYSQL_DB']} default charset = utf8mb4"""
cur.execute(sql)
cur.close()
con.close()

admin = os.environ['ADMIN']
password = os.environ['ADMIN_PASSWORD']

flask_app = app.app
app.db.create_all()
if app.User.query.filter_by(APP_ID=admin).first() is None:
        user = app.User(APP_ID=admin)
        user.hash_password(password)
        app.db.session.add(user)
        app.db.session.commit()
# flask_app.debug = True
# flask_app.run(port=6666, threaded=True)