# -*- coding: utf-8 -*-
"""
Just a sample resource
"""
# System imports
import json
# Third-party imports
import falcon
from news_api.endpoints.vespaSearcher import vespaSearch
# Local imports
#from news_api import settings



class SimpleSearch(object):

    @staticmethod
    def on_get(req, resp):
        """[Get request for search]
        
        Arguments:
            req {[falcon.request]} -- [Falcon request type]
            resp {json} -- [Response of the request return by the server]
        
        Raises:
            falcon.HTTPError -- [In case the request is ill-formed,empty, or the server provide no response]"""
        
        try:

            search_params=falcon.uri.parse_query_string(req.query_string)
            
            if search_params is None or  'query' not in search_params  or len(search_params['query'])==0:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({'status': 'Error','message':'Query is empty'})
            else:
                search_response= vespaSearch(search_params)
                if search_response is not None:
                    resp.status = falcon.HTTP_200
                    resp.body = json.dumps({'status': 'OK','message':'',"result":dict(search_response)})
                else:
                    resp.status = falcon.HTTP_500
                    resp.body = json.dumps({'status': 'Error','message':'Vespa Error'})
                print(req.url)            
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_503,'Error:' , e.message)
        