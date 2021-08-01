import pandas as pd

orders = pd.read_csv('orders.csv')
order_lines = pd.read_csv('order_lines.csv')

def get_orders_by_date(date: str) -> list:
    list_of_order_ids = []
    order_ids = orders.loc[orders["created_at"].str[:10] == date, "id"].tolist()
    return order_ids

print(get_orders_by_date('2021-08-01'))