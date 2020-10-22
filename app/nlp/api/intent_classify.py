# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 12:00 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from flask import Blueprint
from flask import request, abort
from ... import token_auth, g
from . import intent_classify
from . import func_time
import time
intent_classify_api = Blueprint('intent-classify', __name__)

@intent_classify_api.route('/intent-classify', methods=['POST'])
@func_time
@token_auth.login_required
def intent_classify_func():
    start = time.time()
    data = request.get_json()
    query = data.get('text')
    if not query:
        abort(400)
    intent_classify_result = intent_classify(query)
    intent = intent_classify_result['intent']
    intent_pro = intent_classify_result['pros']
    APP_ID = g.user.APP_ID
    id = g.user.id
    return_data = {
        'intent': intent,
        'pros': intent_pro,
        'APP_ID': APP_ID,
        'id': id,
        'time_consume_ignore_auth': time.time() - start,
    }
    return return_data