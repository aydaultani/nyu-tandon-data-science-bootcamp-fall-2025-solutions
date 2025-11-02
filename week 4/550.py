# WITH first_login AS (
#     SELECT
#         player_id,
#         MIN(event_date) AS first_date
#     FROM Activity
#     GROUP BY player_id
# ),
# next_day_login AS (
#     SELECT
#         f.player_id
#     FROM first_login f
#     JOIN Activity a
#       ON a.player_id = f.player_id
#      AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
# )
# SELECT
#     ROUND(
#         (SELECT COUNT(*) FROM next_day_login) * 1.0
#         / (SELECT COUNT(*) FROM first_login),
#         2
#     ) AS fraction;

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    f = (activity.groupby("player_id", as_index=False)["event_date"].min().rename(columns={"event_date": "first_date"}))
    f["next_day"] = f["first_date"] + pd.Timedelta(days=1)

    res = f.merge(activity[["player_id", "event_date"]],left_on=["player_id", "next_day"],right_on=["player_id", "event_date"],how="left")

    r = res["event_date"].notna().sum()
    t = len(f)

    frac = round(r / t, 2) if t else 0.00

    return pd.DataFrame({"fraction": [frac]})
