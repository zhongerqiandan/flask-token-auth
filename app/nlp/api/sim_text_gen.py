# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 2:34 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from . import sim_gen
from flask import Blueprint
from flask import request, abort
from ... import token_auth, g
from . import func_time
import time

gen_api = Blueprint('sim-text-gen', __name__)

@gen_api.route('/sim-text-gen', methods=['POST'])
@func_time
@token_auth.login_required
def sim_text_gen_func():
    start = time.time()
    data = request.get_json()
    query = data.get('query')
    if not query:
        abort(400)
    sim_gen_result, http_code = sim_gen(query)
    sim_questions = sim_gen_result['sim_questions']
    APP_ID = g.user.APP_ID
    id = g.user.id
    return_data = {
        'query': query,
        'sim_questions': sim_questions,
        'APP_ID': APP_ID,
        'id': id,
        'time_consume_ignore_auth': time.time() - start
    }
    return return_data