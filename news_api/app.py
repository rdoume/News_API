# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
import falcon
from falcon_cors import CORS

# Local imports

from news_api.endpoints.models import SimpleSearch, TopEntities, TopClusters

from news_api.connectors.postgres import Postgres

# Create resources
db = Postgres()
simplesearch = SimpleSearch()
entity = TopEntities(db)
clusters = TopClusters(db)


# Create falcon app

public_cors = CORS(allow_all_origins=True)
app = falcon.API(middleware=[public_cors.middleware])
app.add_route("/v1/search", simplesearch)
app.add_route("/v1/entities/", entity)
app.add_route("/v1/clusters/", clusters)
