#!/usr/bin/env python
# encoding: utf-8
"""
File Description: 
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2019-12-02 19:39
"""
import logging
from pprint import pprint
import os
import logstash
from logstash import UDPLogstashHandler


class CustomFormatter(logstash.formatter.LogstashFormatterBase):
    def format(self, record):
        message = {
            '@timestamp': self.format_timestamp(record.created),
            '@message_type': record.getMessage(),
            '@fields': {}
        }
        # Add extra fields
        extra_data = self.get_extra_fields(record)
        message['@fields'].update(extra_data)

        # If exception, add debug info
        if record.exc_info:
            message['@fields'].update(self.get_debug_fields(record))
        pprint(message)
        return self.serialize(message)


class CustomLogstashHandler(UDPLogstashHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formatter = CustomFormatter('ai-platform', None, False)


logstash_logger = logging.getLogger('logstash')
logstash_logger.setLevel(logging.INFO)
logstash_logger.addHandler(CustomLogstashHandler(os.environ['LOGSTASH_HOST'], int(os.environ['LOGSTASH_PORT'])))
