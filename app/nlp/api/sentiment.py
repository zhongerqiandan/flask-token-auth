# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 5:37 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from flask import Blueprint
from flask import request, abort
from ... import token_auth, g
from . import func_time
import requests, time

sentiment_api = Blueprint('sentiment', __name__)

API_KEY = 'pNN25glrNmDTaCQIfvgxZg9u'
API_SECRET = 'RZuxT0Om8gv1T1Aft1dk2pBBe5fZgqRu'
TOKEN = None


def fetch_token():
    global TOKEN
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}'
    response = requests.get(host).json()
    TOKEN = response['access_token']


fetch_token()


def post_request(url, data):
    url = url + '?charset=UTF-8&access_token=' + TOKEN
    response = requests.post(url, json=data).json()
    if 'error_code' in response:
        if response['error_code'] == 110 or response['error_code'] == 111:
            fetch_token()
            post_request(url, data)
        else:
            raise Exception(response['error_msg'] + ' text:' + str(data))
    else:
        return response


def sentiment(text):
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion'
    data = {
        "scene": "talk",
        "text": text
    }
    response = post_request(url, data)
    # optimistic,neutral,pessimistic
    result = {
        'label': response['items'][0]['label'],
        'probs': {each['label']: each['prob'] for each in response['items']}
    }
    return result

@sentiment_api.route('/sentiment', methods=['POST'])
@func_time
@token_auth.login_required
def sentiment_func():
    start = time.time()
    text = request.get_json().get('text')
    if not text:
        abort(400)
    result = sentiment(text)
    APP_ID = g.user.APP_ID
    id = g.user.id
    return_data = {
        'label': result['label'],
        'probs': result['probs'],
        'APP_ID': APP_ID,
        'id': id,
        'time_consume_ignore_auth': time.time() - start
    }
    return return_data