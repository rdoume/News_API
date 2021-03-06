import pendulum


def ordering_cluster(cluster, method="date"):

    if method == "date":
        ordered_cluster = sorted(
            cluster["clusters"], key=lambda k: k["date"], reverse=True
        )
    elif method == "score":
        ordered_cluster = sorted(
            cluster["clusters"], key=lambda k: k["cluster_score"], reverse=True
        )
    else:
        ordered_cluster = sorted(
            cluster["clusters"], key=lambda k: k["size"], reverse=True
        )

    return ordered_cluster


def getTopNewCluster(
    conn, count=5, country="fr", lang="fr", category=None, ordering_method="size"
):
    enum_cat = [
        "main",
        "world",
        "economy",
        "sport",
        "society",
        "culture",
        "tech",
        "politics",
        "health",
    ]
    cur = conn.cursor()
    if count is None:
        count = 5
    if lang is None:
        lang = "fr"
    if ordering_method is None:
        ordering_method = "date"
    if category not in enum_cat:
        category = "main"

    query = """
    SELECT date as date,
           dict as cluster
    FROM public.clusters_table_cat
    WHERE date <= '{0}'
    AND country= '{1}'
    AND category='{2}'
    ORDER BY date DESC
    LIMIT 1;
    """.format(
        pendulum.now(tz='Europe/Paris').to_datetime_string(), country, category
    )
    cur.execute(query)
    datetime, cluster = cur.fetchone()
    ordered_cluster = ordering_cluster(cluster, method=ordering_method)
    count = int(count)
    if count <= 0 or count > len(ordered_cluster):
        count = len(ordered_cluster) - 1

    return ordered_cluster[0:count]
