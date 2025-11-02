# SELECT
#     p.project_id,
#     ROUND(AVG(e.experience_years), 2) AS average_years
# FROM Project p
# JOIN Employee e
#     ON p.employee_id = e.employee_id
# GROUP BY p.project_id;

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    m = project.merge(employee, on="employee_id", how="inner")
    res = (m.groupby("project_id", as_index=False)["experience_years"].mean().round(2).rename(columns={"experience_years": "average_years"}))
    return res
