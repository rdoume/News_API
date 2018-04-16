# -*- coding: utf-8 -*-
"""
Local settings file
"""
# Local imports
# Third-party imports

from redis import StrictRedis


# Local imports
from base import *



REDIS_DB = StrictRedis('localhost')

