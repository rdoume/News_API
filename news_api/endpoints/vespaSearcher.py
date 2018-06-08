import requests
from news_api.settings.Vespa_config import VESPA_IP, VESPA_PORT
import json
from ast import literal_eval


def GenerateDateParamYql(params):
    """[Check consistency in date parameterGenerate the date yql parameters]
    
    Arguments:
        params {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    yql = ""

    if "fromDate" in params:
        if params["fromDate"].isdigit():
            yql += " and published_date > " + str(params["fromDate"])
    if "toDate" in params:
        if params["toDate"].isdigit():
            yql += " and published_date < " + str(params["toDate"])
    if "fromDate" in params and "toDate" in params:
        if params["fromDate"].isdigit() and params["toDate"].isdigit():
            if params["fromDate"] > params["toDate"]:
                return ""
    return yql


def GenerateNewsYql(params):
    """[Generator of YQL vespa query, to have a refine request on the vespa cluster]
    In this case, the YQL depends on the search definition of the document type in the vespa cluster
    Modify with risk, some parameters position are important, such as limit
    
    Returns:
        yql [string] -- [String that select documents based on userquery
    """

    yql = "&yql=select * from sources * where userQuery()"

    if "source" in params:
        yql += ' and hostsite contains " ' + params["source"] + ' "'
    if "language" in params:
        yql += ' and country contains "' + params["language"] + '"'
    yql += GenerateDateParamYql(params)
    if "count" in params:
        if params["count"].isdigit():
            yql += " limit " + str(params["count"])
    if "offset" in params:
        if params["offset"].isdigit():
            yql += " offset " + str(params["offset"])
    return yql


def vespaSearch(params):
    """Search Function for Vespa:
        
        
    Arguments:
            params {dict} -- [Dict containings all parameters for the Vespa Search]
                List of accepted params:
                    :param query: User query to search (required)
                    :param toDate: Maximum datelimit for the publication date (optionnal, default = now() )
                    :param fromDate: Minimum datelimit for the publication date (optionnal)
                    :param count: Number of document to retrieve (optionnal, default = 10)
                    :param offset: Offset for the retrieved documents ( optionnal, default = 0)
                    :param source: Filter for the accepter hostsites (optionnal)
    """
    result = None
    if "query" not in params:
        return None
    else:
        yql = GenerateNewsYql(params)
        try:
            print(
                "http://"
                + VESPA_IP
                + ":"
                + VESPA_PORT
                + "/search/?query="
                + params["query"]
                + yql
                + ";"
            )
            result_request = requests.get(
                "http://"
                + VESPA_IP
                + ":"
                + VESPA_PORT
                + "/search/?query="
                + params["query"]
                + yql
                + ";"
            )
            if result_request.status_code == 200:
                result = result_request.json()
        except Exception as e:
            print(e)
            return None

    return result
