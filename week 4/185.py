# SELECT
#     d.name AS Department,
#     e.name AS Employee,
#     e.salary AS Salary
# FROM Employee e
# JOIN Department d
#   ON e.departmentId = d.id
# WHERE (
#     SELECT COUNT(DISTINCT e2.salary)
#     FROM Employee e2
#     WHERE e2.departmentId = e.departmentId
#       AND e2.salary > e.salary
# ) < 3;

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    res = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    res = res.rename(columns={'name_x': 'Employee', 'name_y': 'Department'})
    res['rnk'] = res.groupby('Department')['salary'].rank(method='dense', ascending=False)
    res2 = res[res['rnk'] <= 3][['Department', 'Employee', 'salary']]
    res2 = res2.rename(columns={'salary': 'Salary'})

    return res2
