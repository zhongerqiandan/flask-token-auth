# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 10:42 上午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

import time, os
from flask import Flask, g, Blueprint, request
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from .utils.NestableBlueprint import NestableBlueprint
from .utils.logger import logstash_logger
# import mysql_config

# initialization
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    os.environ['DIALECT'],
    os.environ['DRIVER'],
    os.environ['MYSQL_USER_NAME'],
    os.environ['MYSQL_USER_PASSWORD'],
    os.environ['MYSQL_HOST_NAME'],
    os.environ['MYSQL_PORT'],
    os.environ['MYSQL_DB']
)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# extensions
db = SQLAlchemy(app)
password_auth = HTTPBasicAuth()
# token_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='jwt')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    APP_ID = db.Column(db.String(32), index=True)
    APP_SECRET_hash = db.Column(db.String(128))

    def hash_password(self, APP_SECRET):
        self.APP_SECRET_hash = generate_password_hash(APP_SECRET)

    def verify_password(self, APP_SECRET):
        return check_password_hash(self.APP_SECRET_hash, APP_SECRET)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'APP_ID': self.APP_ID, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        logstash_logger.info(token)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              algorithms=['HS256'])
        except:
            return
        return User.query.filter_by(id=data['id']).first()

@password_auth.verify_password
def verify_password(APP_ID, APP_SECRET):
    user = User.query.filter_by(APP_ID=APP_ID).first()
    if not user or not user.verify_password(APP_SECRET):
        return False
    g.user = user
    return True

@token_auth.verify_token
def verify_token(token):
    # first try to authenticate by token
    user = User.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True

# from .api import sim_text_gen, user, token
from .nlp import nlp_api
from .users.users import users_api
from .token.token import token_api

api_v1 = NestableBlueprint('jarvis-ai-platform', __name__, url_prefix='/v1')
api_v1.register_blueprint(nlp_api)
api_v1.register_blueprint(users_api)
api_v1.register_blueprint(token_api)
app.register_blueprint(api_v1)

@app.after_request
def after_request(response):
    logger_data = {
        'request.remote_addr': request.remote_addr,
        'request.method': request.method,
        'request.full_path': request.full_path,
        'response.status': response.status,
    }
    request_data = request.get_json()
    response_data = response.data
    logger_data['request.data'] = request_data
    logger_data['response.data'] = response_data
    logstash_logger.info('ai-platform-web', extra=logger_data)
    return response