# -*- coding: utf-8 -*-
"""
Just a sample resource
"""
# System imports
import json
# Third-party imports
import falcon

# Local imports
from news_api import settings


class SampleResource(object):
    """ Just a sample resource model to
    test the falcon app"""

    @staticmethod
    def on_post(req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'OK': 'This is just a test'})
