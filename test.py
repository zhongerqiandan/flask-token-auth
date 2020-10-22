# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 6:36 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

# import requests
#
# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTAsIkFQUF9JRCI6ImRhb2ppYSIsImV4cCI6MTYwNTg0MjM3MC44NTQzNDd9.6Hr3p2ySVeTFZce7OUzKgUEMn5Qsjwwi1iVyuirqZpI'
# auth = ('jww', 'python')
# data = {
#     'APP_ID': "jww",
#     "APP_SECRET": 'python'
# }
# response = requests.post(url='http://127.0.0.1:6666/v1/users', json=data, auth=t_auth)
# print(response.json())
# print(response.status_code)
# print(response.headers)

# response = requests.get(url='http://127.0.0.1:6666/v1/token', auth=auth)
# print(response.json())
# data = {
#     'text': '北京今天的天气如何'
# }
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'JWT {token}'
# }
# response = requests.post(url='http://127.0.0.1:6666/v1/nlp/sentiment', json=data, headers=headers)
# print(response.json())
#
# data = {
#     'query': '北京今天的天气如何',
#     'questions': ['北京今天的天气怎么样']
# }
# response = requests.post(url='http://127.0.0.1:6666/v1/nlp/qq-sim', json=data, auth=t_auth)
# print(response.json())
#
# data = {
#     'query': '北京今天的天气如何'
# }
# response = requests.post(url='http://127.0.0.1:6666/v1/nlp/sim-text-gen', json=data, auth=t_auth)
# print(response.json())
# import requests, time
#
# # sentiment_api = Blueprint('sentiment', __name__)
#
# API_KEY = 'pNN25glrNmDTaCQIfvgxZg9u'
# API_SECRET = 'RZuxT0Om8gv1T1Aft1dk2pBBe5fZgqRu'
# TOKEN = None
#
#
# def fetch_token():
#     global TOKEN
#     host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}'
#     response = requests.get(host).json()
#     TOKEN = response['access_token']
#
#
# fetch_token()
#
#
# def post_request(url, data):
#     url = url + '?charset=UTF-8&access_token=' + TOKEN
#     response = requests.post(url, json=data).json()
#     if 'error_code' in response:
#         if response['error_code'] == 110 or response['error_code'] == 111:
#             fetch_token()
#             post_request(url, data)
#         else:
#             raise Exception(response['error_msg'] + ' text:' + str(data))
#     else:
#         return response
#
#
# def sentiment(text):
#     url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion'
#     data = {
#         "scene": "talk",
#         "text": text
#     }
#     response = post_request(url, data)
#     # optimistic,neutral,pessimistic
#     result = {
#         'label': response['items'][0]['label'],
#         'probs': {each['label']: each['prob'] for each in response['items']}
#     }
#     return result
#
# text = '今天天气很不好'
# start = time.time()
# re = sentiment(text)
# print(re)
# print(time.time() - start)

import requests
import os, time

# admin = 'root'
# admin_pw = 'Qud9ydOVX0ytLC6X'
#
# pw_auth = (admin, admin_pw)
# response = requests.get(url='http://127.0.0.1:6666/v1/token', auth=pw_auth)
# print(response.json())
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiQVBQX0lEIjoicm9vdCIsImV4cCI6MTYwNTg3NTc3NC4xMTI3fQ.U_UvPtDXHBaP77lhS4oYlleNN33QB2bZ0P2hMorwW1E'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'JWT {token}'
}
data = {
    'text': '今天天气怎么样',
}
response = requests.post(url='http://127.0.0.1:6666/v1/nlp/sentiment', json=data, headers=headers)
print(response.json())



# print(type(re))
