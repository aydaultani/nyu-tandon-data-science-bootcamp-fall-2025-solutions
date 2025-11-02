# SELECT
#     p.firstName,
#     p.lastName,
#     a.city,
#     a.state
# FROM Person p
# LEFT JOIN Address a
#     ON p.personId = a.personId;

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    res = person.merge(address, on="personId", how="left")
    return res[["firstName", "lastName", "city", "state"]]

