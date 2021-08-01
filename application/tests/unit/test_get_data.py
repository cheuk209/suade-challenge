import pandas as pd
from dummy_get_data import *

orders = pd.read_csv('orders.csv')
order_lines = pd.read_csv('order_lines.csv')

def test_get_order_ids_by_date():
    orders_expected = get_order_ids_by_date('2021-08-01')
    assert orders_expected == [2,3]

def test_get_orderlines_by_ids():
    order_ids = get_order_ids_by_date('2021-08-01')
    orderlines_quantity_expected = get_orderlines_by_ids(order_ids)
    assert orderlines_quantity_expected == [30, 12, 40, 10, 10, 56]

def test_get_number_items_sold_by_date():
    assert get_total_number_items_sold_by_date('2021-08-01') == 158
    assert get_total_number_items_sold_by_date('2012-09-12') == 0

def test_get_number_customers_by_date():
    assert get_number_customers_by_date('2021-08-01') == 2
    assert get_number_customers_by_date('2021-08-02') == 2
    assert get_number_customers_by_date('2012-09-12') == 0

def test_get_total_discount_amount_by_date():
    assert get_total_discount_amount_by_date('2021-07-31') == 0
    assert get_total_discount_amount_by_date('2021-08-01') == 43

def test_get_average_discount_rates_by_date():
    assert get_average_discount_rates_by_date('2021-07-31') == 0
    assert get_average_discount_rates_by_date('2021-08-01') == 0.2167
    assert get_average_discount_rates_by_date('2021-08-02') == 0.15

def test_get_average_order_total_by_date():
    assert get_average_order_total_by_date('2021-07-31') == 0
    assert get_average_order_total_by_date('2021-08-01') == 41.8333
    assert get_average_order_total_by_date('2021-08-02') == 50.8