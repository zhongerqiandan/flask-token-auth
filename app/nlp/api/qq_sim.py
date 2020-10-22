# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 12:25 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from flask import Blueprint
from flask import request,abort
from ... import token_auth, g
from . import qq_sim
from . import func_time
import time

qq_sim_api = Blueprint('qq-sim', __name__)

@qq_sim_api.route('/qq-sim', methods=['POST'])
@func_time
@token_auth.login_required
def qq_sim_func():
    start = time.time()
    query = request.get_json().get('query')
    questions = request.get_json().get('questions')
    if not query or not questions:
        abort(400)
    qq_result = qq_sim(questions, query)
    qq_sim_time, qq_sim_result = qq_result['time_consume'], qq_result['pros']
    APP_ID = g.user.APP_ID
    id = g.user.id
    return_data = {
        'pros': qq_sim_result,
        'APP_ID': APP_ID,
        'id': id,
        'query': query,
        'questions': questions,
        'time_consume_ignore_auth': time.time() - start
    }
    return return_data