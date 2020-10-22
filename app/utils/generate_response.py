#!/usr/bin/env python
# encoding: utf-8
from flask import jsonify
import logging
from flask import jsonify, make_response


def success(res=None):
    return make_response(jsonify(res), 200)


def error(message):
    import traceback
    logging.error(str(traceback.format_exc()))
    return make_response(jsonify({'message': message}), 400)
