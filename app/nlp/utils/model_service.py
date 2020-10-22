# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 2:40 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

import requests
import os

def intent_classify(query):
    data = {
        'text': query
    }
    return requests.post(os.environ['INTENT_CLASSIFY_SERVICE_URL'], json=data).json()


def qq_sim(questions, query):
    data = {
        "questions": questions,
        "query": query
    }
    return requests.post(os.environ['QQ_SIM_SERVICE_URL'], json=data).json()

#
def sim_gen(query):
    data = {
        'query': query
    }
    return requests.post(os.environ['SIM_GEN_SERVICE_URL'], json=data).json()

# def intent_classify(query):
#     data = {
#         'text': query
#     }
#     return {'intent': 0, 'pros': 0, 'time_consume': 1}
#
#
# def qq_sim(questions, query):
#     data = {
#         "questions": questions,
#         "query": query
#     }
#     return {'time_consume': 0, 'pros': [0.1, 0.9]}
#
#
# def sim_gen(query):
#     data = {
#         'query': query
#     }
#     return ({'sim_questions': ['nihao']}, 200)