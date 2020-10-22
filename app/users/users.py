# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 5:32 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from flask import Blueprint
from flask import abort, request, jsonify, url_for, make_response
# from app.nlp import User, db
from .. import User, db, token_auth, g
import os
users_api = Blueprint('users', __name__)

@users_api.route('/users/add', methods=['POST'])
@token_auth.login_required
def new_user():
    APP_ID = g.user.APP_ID
    if APP_ID != os.environ['ADMIN']:
        abort(401)
    APP_ID = request.json.get('APP_ID')
    APP_SECRET = request.json.get('APP_SECRET')
    if APP_ID is None or APP_SECRET is None:
        abort(400)  # missing arguments

    if User.query.filter_by(APP_ID=APP_ID).first() is not None:
        abort(400)  # existing user

    user = User(APP_ID=APP_ID)
    user.hash_password(APP_SECRET)
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({'APP_ID': user.APP_ID}), 201)

@users_api.route('/users/delete', methods=['POST'])
@token_auth.login_required
def delete_user():
    APP_ID = request.json.get('APP_ID')
    if APP_ID is None:
        abort(400)
    if APP_ID == os.environ['ADMIN']:
        abort(401)
    user = User.query.filter_by(APP_ID=APP_ID).first()
    if user is None:
        abort(400)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({'msg': f'delete {APP_ID}'}), 200)