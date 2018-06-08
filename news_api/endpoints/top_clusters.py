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
    conn, number=5, country="fr", lang="fr", category=None, ordering_method="size"
):
    cur = conn.cursor()
    if number is None:
        number = 5
    if lang is None:
        lang = "fr"
    if ordering_method is None:
        ordering_method = "score"

    query = """
    SELECT date as date,
           dict as cluster
    FROM public.clusters_table
    WHERE date <= '{0}'
    AND country= '{1}'
    ORDER BY date DESC
    LIMIT 1;
    """.format(
        pendulum.now().to_datetime_string(), country
    )
    cur.execute(query)
    datetime, cluster = cur.fetchone()
    ordered_cluster = ordering_cluster(cluster, method=ordering_method)
    number = int(number)
    if number <= 0 or number > len(ordered_cluster):
        number = len(ordered_cluster) - 1

    return ordered_cluster[0:number]