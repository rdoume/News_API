# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
import falcon

# Local imports
from news_api.sample.models import SampleResource

from news_api.endpoints.models import SimpleSearch,TopEntities

from news_api.connectors.postgres import Postgres

# Create resources
intro = SampleResource()
db=Postgres()

simplesearch = SimpleSearch()
entity = TopEntities(db)

# Create falcon app
app = falcon.API()
app.add_route('/v1/search',simplesearch)
app.add_route('/v1/entities/',entity)
app.add_route('/v1/clusters/',simplesearch)



