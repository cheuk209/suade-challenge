import pandas as pd
from get_data import *

orders = pd.read_csv('orders.csv')
order_lines = pd.read_csv('order_lines.csv')

def test_get_orders_by_date():
    orders_expected = get_orders_by_date('2021-08-01')
    assert orders_expected == [2,3]
