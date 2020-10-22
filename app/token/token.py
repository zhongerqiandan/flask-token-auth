# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 6:28 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from flask import Blueprint
from flask import jsonify, g, make_response
from .. import password_auth
import os
import math

token_api = Blueprint('token', __name__)
duration = math.ceil(float(os.environ['TOKEN_DURATION']))
duration = 3600 * duration
# duration = 3600


@token_api.route('/token')
@password_auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(duration)
    APP_ID = g.user.APP_ID
    return make_response(jsonify({'token': token.decode('ascii'), 'duration': duration, 'APP_ID': APP_ID}), 200)