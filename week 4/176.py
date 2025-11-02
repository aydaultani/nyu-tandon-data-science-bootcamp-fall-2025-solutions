# SELECT
#     (
#         SELECT DISTINCT salary
#         FROM Employee
#         ORDER BY salary DESC
#         LIMIT 1 OFFSET 1
#     ) AS SecondHighestSalary;

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    res = sorted(employee['salary'].unique(), reverse=True)
    if len(res) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [res[1]]})
