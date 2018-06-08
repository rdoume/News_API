# -*- coding: utf-8 -*-


def getQueryTopEntity(from_date, to_date, country, category=None, limit=100):
    if category is not None:
        query = """
        SELECT entity AS entity,
            SUM(count) AS "SUM(count)"
        FROM public.human_entities
        WHERE date >= '{0}'
        AND date <= '{1}'
        AND country='{2}'
        AND category='{3}'
        GROUP BY entity
        ORDER BY "SUM(count)" DESC
        LIMIT {4};
        """.format(
            from_date, to_date, country, category, limit
        )
    else:
        query = """
        SELECT entity AS entity,
            SUM(count) AS "SUM(count)"
        FROM public.human_entities
        WHERE date >= '{0}'
        AND date <= '{1}'
        AND country='{2}'
        GROUP BY entity
        ORDER BY "SUM(count)" DESC
        LIMIT {3};
        """.format(
            from_date, to_date, country, limit
        )
    return query


def getQueryUniqueEntity(from_date, to_date, lang, limit, entity):

    query = """
    SELECT entity AS entity,
        SUM(count) AS "SUM(count)"
    FROM public.human_entities
    WHERE date >= '{0}'
    AND date <= '{1}'
    AND country='{2}'
    AND entity='{3}'
    GROUP BY entity
    ORDER BY "SUM(count)" DESC
    LIMIT {4};
    """.format.format(
        from_date, to_date, lang, entity, limit
    )
    return query
