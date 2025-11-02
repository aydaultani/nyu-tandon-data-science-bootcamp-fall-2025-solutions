# SELECT
#     p.product_name,
#     SUM(o.unit) AS unit
# FROM Orders o
# JOIN Products p
#     ON o.product_id = p.product_id
# WHERE o.order_date >= '2020-02-01'
#   AND o.order_date <  '2020-03-01'
# GROUP BY p.product_id, p.product_name
# HAVING SUM(o.unit) >= 100;

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    working_orders = orders[(orders["order_date"] >= "2020-02-01") & (orders["order_date"] <  "2020-03-01")]
    sums = (working_orders.groupby("product_id", as_index=False)["unit"].sum())

    sums = sums[sums["unit"] >= 100]

    res = sums.merge(products[["product_id", "product_name"]], on="product_id", how="inner")

    return res[["product_name", "unit"]]
