import requests
from news_api.settings.Vespa_config import VESPA_IP,VESPA_PORT

def vespaSearch(params):
    """Search Function for Vespa:
        
        
    Arguments:
            params {dict} -- [Dict containings all parameters for the Vespa Search]
            Only one parameter is mandatory : query
    """
    result=None
    if 'query' not in params:
        return None
    else:
        try:
            result= requests.get("http://"+VESPA_IP+":"+VESPA_PORT+"/search/?query="+params['query'])
        except Exception as e:
            print(e)
            return None    
    return result.json()
