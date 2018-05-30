# API to access the news cluster, based on VESPA engine

This API is used to access the news cluster on the vespa engine cluster.
This is a big work in progress, so far, and is used a training for vespa.

## List of API endpoints : 

    - /simplesearch

## List of Parameters per endpoint

### Simple Search:

So far, the following parameters are accepted:

        :param query: User query to search (required)
        :param toDate: Maximum datelimit for the publication date (optionnal, default = now() )
        :param fromDate: Minimum datelimit for the publication date (optionnal)
        :param count: Number of document to retrieve (optionnal, default = 10)
        :param offset: Offset for the retrieved documents ( optionnal, default = 0)
        :param source: Filter for the accepted hostsites (optionnal)


### Similarity Search: