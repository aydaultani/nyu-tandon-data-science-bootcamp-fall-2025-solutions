# SELECT
#     eu.unique_id,
#     e.name
# FROM Employees e
# LEFT JOIN EmployeeUNI eu
#     ON e.id = eu.id;

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = employees.merge(employee_uni, on="id", how="left")
    return res[["unique_id", "name"]]
