# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 11:58 上午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com

from ..utils.NestableBlueprint import NestableBlueprint
from .api.sim_text_gen import gen_api
from .api.qq_sim import qq_sim_api
from .api.intent_classify import intent_classify_api
from .api.sentiment import sentiment_api

nlp_api = NestableBlueprint('nlp', __name__, url_prefix='/nlp')
nlp_api.register_blueprint(gen_api)
nlp_api.register_blueprint(qq_sim_api)
nlp_api.register_blueprint(intent_classify_api)
nlp_api.register_blueprint(sentiment_api)