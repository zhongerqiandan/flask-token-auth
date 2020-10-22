# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 12:22 下午
# @Author  : Jiangweiwei
# @mail    : zhongerqiandan@163.com


from flask import Blueprint

# class NestableBlueprint(Blueprint):
#     def register_blueprint(self, blueprint, **options):
#         def deferred(state):
#             url_prefix = options.get('url_prefix')
#             if url_prefix is None:
#                 print(blueprint)
#                 url_prefix = blueprint.url_prefix
#             if 'url_prefix' in options:
#                 del options['url_prefix']
#
#             state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
#         self.record(deferred)

class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        self.record(deferred)