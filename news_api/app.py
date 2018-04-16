# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
import falcon

# Local imports
from news_api.sample.models import SampleResource

from news_api.endpoints.models import SimpleSearch

# Create resources
intro = SampleResource()
simplesearch = SimpleSearch()


# Create falcon app
app = falcon.API()
app.add_route('/', intro)
app.add_route('/search',simplesearch)


