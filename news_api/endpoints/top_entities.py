import pandas as pd
import pendulum
import numpy as np
from news_api.endpoints.sqlEntityQueries import getQueryTopEntity


def getTopNewEntities(conn, country, category=None, window=-2, limit=100, count=None):
    numday = window
    now = pendulum.now(tz='Europe/Paris')
    all_en = []
    cur = conn.cursor()
    for i in range(0, abs(numday)):
        from_date = now.subtract(days=abs(numday + i)).to_datetime_string()
        to_date = now.subtract(days=abs(numday + i + 1)).to_datetime_string()
        query = getQueryTopEntity(from_date, to_date, country, category)
        # cur = conn.cursor()
        cur.execute(query)
        all_en.append(cur.fetchall())
    dfs = []
    for i, elt in enumerate(all_en):
        dfs.append(
            pd.DataFrame.from_records(elt, columns=["entity", str(i)]).set_index(
                "entity"
            )
        )
    df = pd.concat(dfs, axis=1)
    df["idf"] = np.log10(len(all_en) / df.count(axis=1))
    today = pd.DataFrame.from_records(
        all_en[-1], columns=["entity", "count"]
    ).set_index("entity")
    today["tf"] = today / today.sum()
    today["idf"] = df["idf"]
    today["tfidf"] = today["idf"] * today["tf"]
    # print(number * 2)
    if count is not None:
        list_entities = list(
            today.sort_values(["tfidf"], ascending=False)[0:count].index
        )
    else:
        list_entities = list(today.sort_values(["tfidf"], ascending=False)[0:].index)
    return list_entities
