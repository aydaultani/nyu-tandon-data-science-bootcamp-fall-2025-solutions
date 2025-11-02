# SELECT
#     actor_id,
#     director_id
# FROM ActorDirector
# GROUP BY actor_id, director_id
# HAVING COUNT(*) >= 3;

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    res = (
        actor_director
        .groupby(["actor_id", "director_id"])
        .size()
        .reset_index(name="cnt")
        .query("cnt >= 3")[["actor_id", "director_id"]]
    )
    return res


