# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
import falcon

# Local imports
from news_api.sample.models import SampleResource


# Create resources
sample_resource = SampleResource()


# Create falcon app
app = falcon.API()
app.add_route('/sample_resource', sample_resource)


# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
